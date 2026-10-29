---
type: Method
title: "Detached-eddy simulation and its delayed and zonal forms"
description: "The single-model hybrid RANS/LES in which a RANS model's length scale is capped by a grid length so that the model acts as a subgrid model away from walls; the DES switch and ambiguous grids, DDES shielding, IDDES, ZDES modes including mode 2 (2020), grid lengths, scheme calibration, transitional and adaptive variants, high-order DG use, and applications."
status: established
aliases: [DES, DDES, delayed detached-eddy simulation, IDDES, improved delayed DES, ZDES, zonal detached-eddy simulation, DDES-SST, SST-IDDES, SA-DDES, ZDES mode 2, ZDES mode 0+1, shear-layer-adapted length scale, grey area, DDES-γ, transitional DDES, RSM-IDDES, RSM-DynIDDES, dynamic IDDES, modelled-stress depletion, grid-induced separation, AIDDES, adaptive IDDES, transitional IDDES, SA-BCM IDDES]
tags: [des, hybrid-rans-les, rans, les, turbomachinery, mesh-adaptation]
timestamp: 2026-10-29T16:19:00Z
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

**The original diagnosis.** The paper that introduced DDES,
[Spalart et al. (2006)](/sources/spalart-2006.md), writes the 1997 DES
(DES97) with the Spalart–Allmaras host as
$d_{\mathrm{DES}}=\min(d,C_{\mathrm{DES}}\Delta_{\max})$, with
$C_{\mathrm{DES}}$ "of order 1" and no value printed. Whether to use
$\Delta_{\max}$ or $\Delta_{\mathrm{vol}}$ is called "a separate issue,
present in any LES" (§1). With equal wall-parallel spacings
$\Delta_\parallel$ (page-local), it classes boundary-layer grids in three
types (§1, Fig. 1):

- *Type I*, natural DES: $\Delta_\parallel$ exceeds $\delta$ and
  $d_{\mathrm{DES}}=d$ throughout the boundary layer.
- *Type II*, "ambiguous": the limiter acts "roughly in the upper
  two-thirds of the boundary layer", but the grid cannot support resolved
  fluctuations.
- *Type III*, an LES grid: all spacings are much smaller than $\delta$;
  $\Delta\approx\delta/20$ is "a plausible starting value", and
  $\Delta\approx\delta/10$ "gives acceptable results". DES formulas on
  this grid amount to a [wall-modelled LES](/methods/wall-modelled-les.md).

On a Type II grid the limiter lowers the eddy viscosity and the modelled
stress "without any sizeable resolved stress to restore the balance",
which the authors name **modeled-stress depletion (MSD)**. It arises on
grid refinement from Type I or when a boundary layer thickens near
separation; the same grid can be Type I at one angle of attack and Type
II at another. Severe MSD gives the "grid-induced separation" of Menter
and Kuntz (cited). The authors add that DES is not "a coarser-grid version
of LES": it "differs from LES only in boundary layers", and the contrary
idea "has led to several inappropriate comparisons between LES and DES"
(§1). MSD faces any hybrid that puts the grid spacing into the turbulence
model. Methods without it, scale-adaptive simulation and TRRANS (cited),
reach LES behaviour in homogeneous turbulence, but "neither approach has
been able to sustain LES content in a channel" (§1; see
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md)). The
earlier remedies are judged not robust enough: manual zonal disabling of
the limiter, cell-aspect-ratio biasing, and the modified length
$\min\big(C_{\mathrm{DES}}\max(n^2C_{\mathrm{DES}}\Delta^2/d,\Delta),d\big)$,
$n=3$, of Forsythe et al. (cited) (§1).

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

**The original form.** [Spalart et al. (2006)](/sources/spalart-2006.md)
(§2.1, Eqs. 2.1–2.3) define, for any eddy-viscosity model,

$$r_d=\frac{\nu_t+\nu}{\sqrt{\partial_ju_i\,\partial_ju_i}\;\kappa^2d^2},\qquad f_d=1-\tanh\big[(8r_d)^3\big],\qquad d_{\mathrm{DDES}}=d-f_d\max\big(0,\,d-C_{\mathrm{DES}}\Delta\big),$$

with $\Delta=\Delta_{\max}$; their $\sqrt{U_{i,j}U_{i,j}}$ is the norm of
the full velocity gradient, written here with the summed indices in the
same order, and $\kappa$ has no printed value. "Similar to $r$ in the S-A
model", $r_d$ is 1 in a logarithmic layer and falls gradually to 0
towards the boundary-layer edge. The added $\nu$ keeps $r_d$ away from 0
very near the wall, and "in the S-A model, $\tilde\nu$ can be used instead
of $\nu_t+\nu$". The "d" stands for "delayed". $f_d$ is 1 in the LES
region ($r_d\ll1$) and 0 elsewhere, "similar to $1-F_2$, and rather steep
near $r_d=0.1$". The constants 8 and 3 come from "intuitive shape
requirements" and flat-plate tests. A constant larger than 8 "would delay
LES in even larger regions, which would be safer in the sense of avoiding
MSD, but is undesirable overall", and models very different from SA
might need "a modest adjustment of $f_d$". $f_d=0$ gives RANS
($d_{\mathrm{DDES}}=d$) and $f_d=1$ gives DES97; for other hosts, DDES
multiplies by $f_d$ "the term that constitutes the difference between RANS
and DES" (§2.1). Because the length now depends on the eddy-viscosity
field, it is time-dependent and RANS mode is "self-perpetuating" in
boundary layers. After massive separation LES takes over "more abruptly
following separation than in DES97", which narrows the grey area: this
speeds the growth of resolved content without creating it (§2.2). DDES,
like $F_2$, does not address MSD in free shear layers, where DES grids are
normally fairly isotropic (§2.2).

*Tests* (two codes; §3). On a flat plate with $\Delta\approx0.1\delta$,
DES97 lowers the peak eddy viscosity by about 75% and the skin friction by
19% from RANS, while DDES "preserves the eddy viscosity almost fully"
(§3.2, Fig. 2; see [turbulent boundary layer](/benchmarks/turbulent-boundary-layer.md)).
On the circular cylinder at $Re_D=10^5$ with laminar separation the two
give the same pressure distribution (§3.3, Fig. 3; see
[circular-cylinder wake](/benchmarks/circular-cylinder-wake.md)). On an
airfoil at $Re_c=2.1\times10^6$ and $13.3^\circ$ incidence, whose
boundary layer reaches about 7% of the chord or 14 cell sizes, the
grid-induced separation of DES97 at $x/c=0.77$ "has been corrected by the
$f_d$ term" (§3.4, Figs. 4–5). On the
[backward-facing step](/benchmarks/backward-facing-step.md) the
opposite-wall friction no longer drops (§3.5). On a multi-element airfoil
at $Re_c=1.8\times10^6$ the main-element boundary layer keeps its eddy
viscosity while the coves and the flap wake keep their resolved content
(§3.6, Figs. 9–11). In a temporal channel started from a RANS field near
one wall and an LES field near the other on a Type III grid, "LES mode
'invaded' RANS mode" (§3.5, no figure). The authors conclude that MSD
would then occur "only in extreme grids" and that the $f_d$ form "appears
simple and permanent enough to be recommended" (§5).

**Later printed forms.** Delayed DES (DDES) detects the boundary layer with a sensor built from the
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
$\tilde\nu$ (footnote 2). The original (above) prints $\nu_t+\nu$ in the
numerator, allows $\tilde\nu$ in place of the whole sum, and puts the
summed indices of the gradient norm in the same order, where François et
al. print $\partial_ju_i\,\partial_iu_j$. The two norms differ: in a pure
shear $u(y)$ the contracted product $\partial_ju_i\,\partial_iu_j$ is zero
while $\partial_ju_i\,\partial_ju_i=(\partial_yu)^2$ *(compiler check, not
in the sources)*. The printed forms stand side by side. Yan et al. (2022) recall the same function as
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
For SA, $l_{\mathrm{RANS}}=d$ and with $f_d=1$ and $\Psi=1$ the form reduces to the
$d_{\mathrm{DES}}$ above *(compiler check, not in the sources)*.

**The low-Reynolds-number correction $\Psi$.** Spalart et al. (2006,
§4.2) introduce $\Psi$ as $l_{\mathrm{DES}}=\min(l_{\mathrm{RANS}},\Psi C_{\mathrm{DES}}\Delta)$
with $\Psi\ge1$, an increased effective $C_{\mathrm{DES}}$. It keeps the
low-Reynolds-number damping terms of SA ($f_{v1}$, $f_{v2}$, $f_{t2}$)
from acting in LES mode at low subgrid viscosity. The hypothesis is that
at "equilibrium" (convection and diffusion negligible) the subgrid model
reduces to a Smagorinsky-like $\nu_t=(C_{\mathrm{eq}}\Delta)^2S$, with
$C_{\mathrm{eq}}$ constant and $S$ a strain magnitude ($C_{\mathrm{eq}}$,
$S$ page-local, $S$ not defined in the paper). With the SA functions of the [Spalart–Allmaras](/methods/spalart-allmaras-model.md)
page and $f_w^*=0.424$ the high-viscosity limit of the equilibrium $f_w$
($f_w^*$ page-local),

$$\Psi^2=\min\left[10^2,\ \frac{1-\dfrac{c_{b1}}{c_{w1}\kappa^2f_w^*}\big[f_{t2}+(1-f_{t2})f_{v2}\big]}{f_{v1}\max\big(10^{-10},\,1-f_{t2}\big)}\right],$$

after the exact form with $f_w/f_w^*$ in the numerator. That ratio is 1
within 2% for $\nu_t>\nu/10$, which allows the simplification. The cap
($\Psi\le10$) and the limiter on $1-f_{t2}$ keep the behaviour reasonable
in the "DNS limit" $\nu_t<\nu/100$. The correction is inactive ($\Psi=1$)
for subgrid viscosity above about $10\nu$ (§4.2, Eqs. 4.3.1–4.3.4, Fig.
12). In a $64^3$ LES of decaying isotropic turbulence its effect on the
eddy viscosity is large (Fig. 12c). In SA-based DDES, $\chi$ is replaced
by $\max(\chi,20f_d)$ before it enters $f_{v1}$ and $f_{t2}$. For
Wilcox's [$k$-$\omega$ model](/methods/k-omega-model.md) the paper gives
$\Psi=(\beta^*/C_\mu)(2a_{\mathrm{Wk}}/a^*_{\mathrm{Wk}})^{3/4}$ with
$a_{\mathrm{Wk}}$, $a^*_{\mathrm{Wk}}$ (page-local; the paper's $\alpha$,
$\alpha^*$) and $C_\mu$, $\beta^*$ "the constants and 'low-Reynolds-number'
functions of the model", and $C_{\mathrm{DES}}=0.72$ for that model's
subgrid version, calibrated on decaying isotropic turbulence, with
$\Psi C_{\mathrm{DES}}\Delta$ replacing $l_{\mathrm{RANS}}$ only in the
dissipation term of the $k$ equation (§4.2, footnote 1).

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
[Tomboulides et al. (2025)](/sources/tomboulides-2025.md), §4); Kumar et
al. (2025) build the second (below).

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

### SST-DDES with a filtered eddy viscosity and an adaptive grid scale

Guo & Wang (2025) sort DES improvements into three groups, the LES length
scale, the delay function and a reformulated eddy viscosity, and cite the
recalibrations of the delay constant: Probst et al. raised $C_{d1}$ from 8
to 16, Jain et al. validated 14 and found 16 over-shielding in
quasi-two-dimensional flat-plate flow, and Gritskevich et al. took 20 for
SST-DDES ([Guo & Wang (2025)](/sources/guo-2025.md), §1, as cited). Their
base is the SST-DDES of Gritskevich et al. in OpenFOAM-v2306 with
$f_d=1-\tanh[(20r_d)^3]$, the kinematic $r_d$ of Möller et al. above, and
the LES coefficient printed as $C_{\mathrm{DDES}}=0.78F_1+0.61F_2$ (Eqs. 6–9;
see the [SST page](/methods/k-omega-sst-model.md)), with the SST blending
function $F_2$ in the second term, where Delassaux et al. (above, Eq. 9)
print $0.78F_1+0.61(1-F_1)$. On it they combine two
changes into ADD-SSTFDDES (§2.1):

- **Filtered eddy viscosity** (SSTFDDES, from the authors' earlier SSTFDES):
  with $L_t=\sqrt k/(\beta^*\omega)$ and a resolvable filter width
  $\Delta_{\mathrm F}=3\max\{\lvert\boldsymbol u\rvert\delta t,\Delta^{1/3}\}$
  ($\delta t$ the time step; $L_t$, $\Delta_{\mathrm F}$ page-local),
  $$\nu_t=\Big(\frac{\min(L_t,\Delta_{\mathrm F})}{L_t}\Big)^{4/3}\frac{a_1k}{\max(a_1\omega,\lvert\Omega\rvert F_2)}$$
  (Eqs. 10–13): the SST viscosity is unchanged where $L_t\le\Delta_{\mathrm F}$
  and reduced otherwise, "to suppress excessive eddy viscosity and
  promot[e] the development of small-scale turbulent fluctuations". The
  viscosity replaces the DDES one in OpenFOAM's `correctNut()`; whether the
  $l_{\mathrm{DDES}}$ destruction is also kept is not stated.
- **Adaptive grid scale** $\Delta_{\mathrm{add}}$ (page-local) in
  $l_{\mathrm{LES}}=C_{\mathrm{DES}}\Delta_{\mathrm{add}}$:
  $\Delta_{\mathrm{add}}=\Delta_{\max}$ where $f_d<0.99$ (boundary layer) or
  $\mu_t/\mu<0.2$ ("a laminar-like flow"), and the least-squares length
  $\Delta_{\mathrm{lsq}}$ of Trias et al. elsewhere, that is in separated
  regions (Eq. 15). $\Delta_{\mathrm{lsq}}$ is built from the velocity
  gradient and a diagonal matrix of grid-related weights (Eq. 14, not
  further explained), and is chosen for its robustness to grid anisotropy;
  $\Delta_{\max}$ is called "overly conservative in the initial shear layer"
  (§2.1).

The four combinations (base or filtered viscosity, $\Delta_{\max}$ or
$\Delta_{\mathrm{add}}$) run with wall functions on a
[square cylinder](/benchmarks/square-cylinder-flow.md) at $Re_D=21\,400$
(4.08 million cells, 64 cores, about 288 core-hours) and on the
[periodic hill](/benchmarks/periodic-hill.md) at $Re_h=10\,565$
($200\times160\times160$) (§2.2, §3). Integral values of the cylinder
(Table 4):

| Model | $St$ | $\langle C_D\rangle$ | $C_L^{\mathrm{rms}}$ | $C_D^{\mathrm{rms}}$ | $L_R/D$ |
|---|---|---|---|---|---|
| SST-DDES, $\Delta_{\max}$ | 0.127 | 2.43 | 1.26 | 0.28 | 1.46 |
| SST-DDES, $\Delta_{\mathrm{add}}$ | 0.120 | 2.74 | 1.43 | 0.17 | 1.27 |
| filtered, $\Delta_{\max}$ | 0.135 | 2.48 | 1.43 | 0.26 | 1.39 |
| filtered, $\Delta_{\mathrm{add}}$ (ADD-SSTFDDES) | 0.127 | 2.71 | 1.60 | 0.20 | 1.42 |
| DNS, Trias et al. ($Re=22\,000$), as listed | 0.132 | 2.18 | 1.71 | 0.205 | 1.04 |
| experiment, Lyn et al., as listed | 0.13 | 2.1 | — | — | 1.4 |

($L_R$ the recirculation length from the cylinder centre, page-local.)
All four mean drags exceed the listed DNS and experiment; the authors place
them inside the range of the LES compilation of Rodi (2.17–2.77) and judge
ADD-SSTFDDES best overall by its fluctuating forces, wake structures and
reattachment, the baseline showing delayed separation and a narrow initial
wake (§3.1, Figs. 10–15). On the hill, the combined model best captures the
near-wall reverse-flow plateau at $x/H=2$ and the $\langle u'u'\rangle$ peak
at $x/H=0.5$, while the baseline overpredicts the $\langle v'v'\rangle$ peak
at $x/H=6$ (§3.2, Figs. 22–25; $H$ the hill height). Most comparisons are
statements about figures; there is no grid study in the paper (it refers to
the earlier one) and no cost comparison among the four models.

**A shielded von Kármán length.** Wang et al. (2024c) apply the SA-DDES
shielding function to the von Kármán length of an SA-based scale-adaptive
model, $d-f_d\max(0,d-L_{\mathrm{vK},3}/\kappa)$, and state that $r_d$ "is
equivalent to" the inverse of the mesh Reynolds number
$\rho\lvert S\rvert\Delta^2/\mu$ ([Wang et al. (2024c)](/sources/wang-2024-j.md),
§III.F, Eqs. 38–40; details on
[scale-adaptive simulation](/methods/scale-adaptive-simulation.md)). On a
Mach 2 boundary layer their SA-DES ($C_{\mathrm{DES}}=0.65$,
$\Delta_{\max}$) and SA-DDES show log-layer mismatch on a coarse grid, which
they call "the inherent defect of original DES method and its variants",
and the DES and DDES interfaces, evaluated on their LES fields, move
toward the wall with grid refinement (§III.B, §III.F, Figs. 1, 15; see
[log-layer mismatch](/definitions/log-layer-mismatch.md)).

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

### Adaptive IDDES: a local LES coefficient from SATES

[Wu et al. (2026)](/sources/wu-2026-b.md) print the SST-IDDES of
Gritskevich et al. (as cited) as

$$l_{\mathrm{IDDES}}=\hat f_d(1+f_e)\,l_{\mathrm{RANS}}+(1-\hat f_d)\,l_{\mathrm{LES}},\qquad l_{\mathrm{LES}}=C_{\mathrm{DES}}\Delta,\qquad \Delta=\min\big[C_w\max(d,\Delta_{\max}),\,\Delta_{\max}\big],$$

with $C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1)$ and $l_{\mathrm{RANS}}=\sqrt k/(\beta^*\omega)$
(the SATES integral length $L_i$, registry §11); $\hat f_d$, $f_e$ and the
value of $C_w$ are not printed (§2.3, Eqs. 17–19). Their grid length has no
wall-normal spacing term, where Carlsson et al. and Li et al. (2024b) above
print $\max(C_wd,C_w\Delta_{\max},\Delta_{wn})$. Their *adaptive IDDES*
(AIDDES) replaces the LES length by

$$l_{\mathrm{LES}}=C_{x,\mathrm{II}}\,\Delta_{\mathrm{vol}},$$

with $C_{x,\mathrm{II}}$ (page-local) the two-layer coefficient of SATES-II,
a WALE-type near-wall coefficient blended with a σ-model coefficient by a
modified SST $F_2$ (Eq. 20; formulas on the
[SATES page](/methods/self-adaptive-turbulence-eddy-simulation.md)). They
read the ratio $l_{\mathrm{IDDES}}/l_{\mathrm{RANS}}$ as a SATES-like
resolution indicator, one in RANS regions (Eq. 21). In SST-IDDES this ratio
stays near 1 in the attached boundary layer, the shielding, but "decays more
slowly and remains at moderate values" in the separated shear layer of a
supersonic base flow, a delayed RANS-to-LES transition; AIDDES keeps the
shielding and drops quickly in the shear layer (§4.1.2, Fig. 8). On the
[supersonic axisymmetric base flow](/benchmarks/supersonic-axisymmetric-base-flow.md)
($M_\infty=2.46$, $9.5\times10^6$ cells) the recirculation length is
$3.58R$ with IDDES and $2.81R$ with AIDDES against $2.63R$ measured
($+36.1\%$ and $+6.8\%$, $R$ the base radius, page-local), at 45.30 and
46.54 wall-clock hours on 640 cores (Table 3); on the
[30P30N airfoil](/benchmarks/30p30n-high-lift-airfoil.md) at $21^\circ$
IDDES suppresses the Kelvin–Helmholtz instability of the slat wake,
giving a "relatively stable quasi-two-dimensional" wake, and AIDDES gives
stronger three-dimensional fluctuations and better velocity profiles
downstream under the varying adverse pressure gradient, while IDDES,
through its shielding, deviates much less near the walls than SATES-SM
(§4.2.2–§4.2.3, Figs. 13–14). On a flat plate, the authors state, AIDDES
does not adversely affect the wall modelling of IDDES (§2.4, Fig. 1). The authors present the adaptive
coefficient as a strategy transplantable to other hybrids (§5).

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

### Transitional IDDES with an algebraic intermittency

[Alberti et al. (2026)](/sources/alberti-2026.md) build a transitional
SA-IDDES in the incompressible modal DG solver of Alberti et al. (2025)
(section on high-order DG below), with the IDDES length of Shur et al., $C_{\mathrm{DES}}=0.65$,
the shear-layer-adapted vorticity length replacing the whole IDDES grid
length, all lengths normalized by $N+1$ and no low-Reynolds-number
correction (§2.1, Eqs. 1–5). Its RANS branch is the algebraic SA-BCM
transition model of Cakmakcioglu et al. (as cited), whose intermittency
$\gamma_{\mathrm{BC}}\in[0,1]$ (page-local; no transport equation) multiplies
the SA source (see
[local-correlation-based transition models](/methods/local-correlation-based-transition-model.md)).
They argue that an algebraic model suits a hybrid because it adds no
equation, and that DES-like models by default cannot predict
laminar-to-turbulent evolution (§1). Three changes against what they call a "standard"
SA-BCM-in-IDDES implementation (§2.1.1):

1. both production and destruction of $\tilde\nu$ are multiplied by
   $\gamma_{\mathrm{BC}}$ (pure-RANS SA-BCM multiplies production only),
   retained from Yalçın et al. (as cited) to keep the eddy-viscosity balance
   in LES mode (Eq. 6);
2. a modified shielding function
   $$\hat f_d^*=\max\{\hat f_d,\,1-\gamma_{\mathrm{BC}}\},$$
   active wherever $\gamma_{\mathrm{BC}}<1$, which forces the sequence
   laminar (Navier–Stokes) → RANS → LES and prevents a switch from a laminar
   solution directly to LES when transition occurs outside the shielded
   region; for DDES the analogue is $f_d^*=\min\{f_d,\gamma_{\mathrm{BC}}\}$
   with the DDES $f_d$ above (Eq. 9; page-local $\hat f_d^*$, $f_d^*$);
3. the SA-BCM constant the source calls $\chi_2$ (here $C_{\mathrm{BC}2}$,
   page-local, not the SA ratio $\chi$) raised from 50 to 1000, to calibrate
   the onset of natural transition; recommended only for DES-like models,
   because the authors observed that 1000 "can already alter pure RANS
   solutions" (§2.1.1, §4).

They state that changes 1 and 2 apply to every intermittency-based
transitional DES-like model, without testing a non-algebraic one, and list
other routes in the literature: an intermittency threshold below which RANS
is enforced (Xiao et al.) and a blending between transitional RANS and DES
(Kim & Kwon), both as cited (§2.1.1, §4).

**Results** (modal DG, $N=3$–5; §3):

- *Eppler 387, $Re_c=3\times10^5$.* Fully turbulent IDDES misses the
  [laminar separation bubble](/definitions/laminar-separation-bubble.md) at
  $0^\circ$ and predicts attached flow; the transitional hybrids match
  transitional RANS in attached flow, which the authors want, since
  switching to LES without massive separation leaves a dissipative deficit
  on DES grids; $C_{\mathrm{BC}2}=1000$ slightly suppresses the bubble at
  $0^\circ$ but places natural transition at $x/c\approx0.2$ at $8^\circ$, as
  measured; at $16^\circ$ the modified model at $N=5$ predicts stall on the
  whole suction side ($C_L=1.169$, $C_D=0.300$ against $C_L=1.09$,
  $C_D=0.25$ and $C_L=0.99$ in two experiments), while fully turbulent IDDES
  gives $C_L=1.427$ (§3.1, Table 3; see
  [Eppler 387 airfoil](/benchmarks/eppler-387-airfoil.md)). With the original
  shielding the Eppler results are "practically identical" (not shown).
- *Sphere at $Re_D=420\,000$* (supercritical; $N=3$, 4): with
  $C_{\mathrm{BC}2}=1000$ all transitional variants show natural transition
  before turbulent separation; with the original shielding refinement from
  $N=3$ to 4 moves transition upstream from $102^\circ$ to $79^\circ$
  (angle from the stagnation point), with $\hat f_d^*$ it stays at
  $97^\circ$–$96^\circ$; the modified model gives $C_D=0.095$ ($N=3$) and
  0.083 ($N=4$), transition at $96^\circ$ and separation at $118^\circ$,
  against Achenbach's $C_D=0.085$, $98^\circ$ and $119^\circ$, and
  transitional RANS gives $C_D=0.375$ (§3.2, Table 5, Fig. 11). The
  free-stream eddy-viscosity ratio $\tilde\nu_\infty/\nu=0.001$ was chosen to put
  onset at the measured location (§3.2, Table 1).
- *NACA 0012 at $11.5^\circ$, $Re_c=1.3\times10^5$.* At $N=4$ both
  transitional variants reproduce the low-frequency burst and reformation
  cycle of the leading-edge bubble, $St=0.0077$ and 0.0097 against 0.008 and
  0.0083 in the references, with $C_D=0.127$ equal to a cited LES at "about
  two orders of magnitude fewer DOFs" and a time step "roughly 50 times
  larger" (stated); the solver behaves globally as WMLES once stalled and
  never returns to pure RANS (§3.3, Table 7; see
  [NACA 0012 airfoil](/benchmarks/naca-0012-airfoil.md)). The equivalent
  Smagorinsky constant $C_{S,\mathrm{eq}}$ of the DG section below, with
  $\Delta_{\mathrm{vol}}$, is about 0.5 in RANS-dominated regions and 0.1–0.2
  over most of the LES region, with a plateau at 0.14 at $x/c=0.4$, so that
  the LES branch "resembles an explicit LES", not an implicit one (Eq. 14,
  Fig. 16).

The authors concede that in natural transition SA-BCM is triggered by its
eddy-viscosity term rather than by its vorticity-Reynolds-number term, so
the onset depends on $\tilde\nu_\infty/\nu$ and $C_{\mathrm{BC}2}$, and leave a
general fix to future work (§3.1–§3.2, §4).

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
| SST-DDES in OpenFOAM (ADD-SSTFDDES) | $\Delta_{\max}$ in boundary layers and where $\mu_t/\mu<0.2$, least-squares $\Delta_{\mathrm{lsq}}$ of Trias et al. elsewhere; $C_{\mathrm{DDES}}=0.78F_1+0.61F_2$ as printed | Guo & Wang (2025), §2.1, Eqs. 7, 14–15 |
| SA-DES and SA-DDES in a finite-difference LES code | $\Delta_{\max}$, $C_{\mathrm{DES}}=0.65$ (the $\Delta$ of DDES not stated) | Wang et al. (2024c), §III.F, Eqs. 29, 37–38 |
| SA-DDES and SA-IDDES in a high-order modal DG code | $\Delta_{\max}$, IDDES $\Delta$, $\Delta_{\mathrm{llm}}$ or $\Delta_\omega$, each divided by $s_\Delta$ (default $N+1$); cell sides from an equivalent hexahedron; $C_{\mathrm{DES}}=0.65$ | Alberti et al. (2025), §2.1–§2.3 (below) |
| DES in general, as surveyed | "the diameter of the cell" (elsewhere the wall-parallel spacing), $C_{\mathrm{DES}}=0.65$ | Luckring & Rizzi (2024), §2.4.1.4 |

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

Spalart et al. (2006, §1) print no value of $C_{\mathrm{DES}}$ for the SA
host, only "of order 1"; the value 0.65 in the paragraph below and in the
SA rows above comes from the later sources. For the Wilcox $k$-$\omega$
subgrid version they give 0.72 (§4.2, footnote 1).

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

## DDES and IDDES in a high-order discontinuous Galerkin solver

Alberti et al. (2025) compare non-zonal SA-based DDES and IDDES variants in
an incompressible modal DG solver (orthonormal hierarchical basis of
complete polynomials of degree $N$, artificial-compressibility Godunov
flux, BR2 viscous flux, linearly implicit Rosenbrock time stepping), since
DES-type models were built for low-order finite volumes and earlier DG work
compared no variants ([Alberti et al. (2025)](/sources/alberti-2025-b.md),
§1–§2). They keep $C_{\mathrm{DES}}=0.65$, calibrated on decaying isotropic
turbulence with a high-order finite-difference scheme and, they state,
confirmed for modal DG on the Taylor–Green vortex by Basile et al.
(§2.1, as cited).
Page-local symbols: $s_\Delta$ the normalization of the grid lengths,
$N_{\mathrm{dof}}=(N+1)(N+2)(N+3)/6$ the degrees of freedom per element,
$\Delta_{\mathrm{llm}}$ Reddy et al.'s length, $\Delta_{dw}$ the IDDES
length (above; the source's $\Delta_{hwn}$, $C_w$ not printed), $\alpha_{\mathrm{ID}}=0.25-d/\Delta_{\max}$
and $f_B=\min\{2\exp(-9\alpha_{\mathrm{ID}}^2),1\}$ the IDDES grid variable and
function, $C_{S,\mathrm{eq}}=\sqrt{\nu_t/(\Delta_{\mathrm{vol}}^2\lvert\Omega\rvert)}$
the equivalent Smagorinsky constant (Eq. 25).

**Grid lengths for high order.** All lengths are divided by $s_\Delta$, taken
as $N+1$, $N$ or $N_{\mathrm{dof}}^{1/3}$, the last suited to a complete
(non-tensor) basis; the ratios $(N+1)/N_{\mathrm{dof}}^{1/3}$ run from 1.26 at
$N=1$ to 1.60 at $N=6$ and both ratios tend to 1.82 as $N\to\infty$ (§2.3,
Table 1). The cell sides of a distorted or curved element come from an
*equivalent hexahedron* with the element's principal moments of inertia
$I_{x'}$, $I_{y'}$, $I_{z'}$ (page-local), rescaled to the element volume $V$,
$$\Delta_x=\Big(V\frac{I_{x'}}{\sqrt{I_{y'}I_{z'}}}\Big)^{1/3},$$
and cyclically, exact for Cartesian cells; tetrahedra and prisms are left
to future work (Eq. 23, Fig. 1). The candidate lengths are
$\Delta_{\max}$, $\Delta_{dw}$, Reddy et al.'s
$\Delta_{\mathrm{llm}}=f_d\Delta_{\mathrm{vol}}+(1-f_d)\Delta_{\max}$ ($\Delta_{\max}$ in
shielded RANS regions, $\Delta_{\mathrm{vol}}$ outside; with $1-\hat f_d$ for $f_d$
in IDDES) and the vorticity-oriented $\Delta_\omega$ of the
shear-layer-adapted length above; $\Delta_{\mathrm{vol}}$ alone is rejected
for switching prematurely to LES in stretched wall cells, and
$\Delta_{\mathrm{SLA}}$ because its averaging over neighbouring cells "loses
meaning" in DG (Eqs. 13, 17–18).

**Findings** (channels at $Re_\tau=400$ and 5200, $N=6$; the
[backward-facing step](/benchmarks/backward-facing-step.md) of Adams's
experiment at $Re_H=28\,000$, $N=3$–4, non-turbulent inflow; [NACA 0012](/benchmarks/naca-0012-airfoil.md)
at $45^\circ$, $Re_c=10^5$; §3):

- **The low-Reynolds-number correction is detrimental.** With $\Psi$ the
  LES branch is forced to $C_{S,\mathrm{eq}}=0.2$, near Lilly's 0.18; without
  it the model still settles at a constant $C_{S,\mathrm{eq}}$, about 0.2 on
  coarse grids and about 0.01 (implicit-LES-like) on fine ones, which the
  authors ascribe to $f_{v1}$, $f_{v2}$; at $Re_\tau=5200$ $\Psi\approx1$ anyway
  for $\tilde\nu/\nu>20$. They recommend letting $\tilde\nu$ evolve freely
  (§3.1.1–§3.1.2, Figs. 5, 10).
- **Lengths.** $\Delta_{\max}$ gives too much eddy viscosity in the grey area,
  shifting $u^+$ upward in the channel and delaying or suppressing the
  Kelvin–Helmholtz instability behind the step; $\Delta_{\mathrm{llm}}$ and
  $\Delta_\omega$ "unlock the complete development" of the rolls and perform
  best; $\Delta_{dw}$ drops the eddy viscosity too sharply in the
  transition and gives visible log-layer mismatch at $Re_\tau=5200$, which the
  authors attribute to the faster wall-normal growth of DG meshes, a
  "staircase progression" of $\Delta_{dw}$ (§3.1–§3.2, Figs. 2, 4, 6,
  9, 12, 16–18).
- **Shielding.** On the fine $Re_\tau=400$ grid $f_d$ shields weakly, because
  the eddy viscosity is small, so DDES shows sporadic unshielded patches and
  slight modelled-stress depletion, while IDDES, through the grid-only
  $f_B$, keeps a shield of constant thickness and gives the best $u^+$, "even
  surpassing an ILES carried out on a much finer grid"; at $Re_\tau=5200$
  $f_d$ dominates and DDES and IDDES nearly coincide for the same length:
  "the shielding function and the SLS are the two key aspects determining
  the final solution" (§3.1.1–§3.1.2, Figs. 2–4, 11).
- **The elevating function.** Enlarging the IDDES protection
  ($\alpha_\xi=0.25-d/(\xi\Delta_{\max})$, $\xi=2$) helps while the interface
  stays in the buffer or lower log layer; Han et al.'s
  $\alpha_{\mathrm{mod}}=1.35-d/\Delta_{\max}$ activates $f_e$ inside the
  shielded zone and corrupts the RANS branch, and on the NACA 0012 $f_e$ is
  active inside the shield and can double the effective wall distance, so
  the authors suggest recalibrating or removing it (§3.1.1, §3.3, Figs. 8,
  25–26).
- **Normalization and order.** The smaller $s_\Delta$, the thicker the shield,
  because $s_\Delta$ also enters $f_B$; $s_\Delta=N+1$ performs best across
  degrees, while $N_{\mathrm{dof}}^{1/3}$, and $N$ at low and moderate degree,
  move too fast toward RANS (on the $Re_\tau=5200$ grid with $N=2$ and
  $s_\Delta=N$ the shielded interface reaches the centreline). Raising $N$ on
  a fixed mesh lowers the eddy viscosity and moves the interface wallward;
  at roughly equal degrees of freedom the highest $N$ is the most accurate
  (§3.1.3, Tables 3–5, Figs. 13–14).

| $Re_\tau=5200$, DDES($\Delta_{\mathrm{llm}}$): mesh, $N$ | DOFs | interface $y^+$, $s_\Delta=N+1$ | $s_\Delta=N$ | $s_\Delta=N_{\mathrm{dof}}^{1/3}$ |
|---|---|---|---|---|
| C, 6 | 32 256 | 1399.8 | 1718.4 | 2672.2 |
| M, 4 | 32 725 | 1446.4 | 2030.8 | 2485.6 |
| F, 2 | 30 720 | 1853.6 | 5200.0 (fully RANS) | — |
| VF, 2 | 60 000 | 1231.9 | — | — |

(Table 5; interface at $f_d=0.1$.) On the step, all variants but standard
DDES and IDDES improve markedly on RANS in $C_f$, standard DDES delaying
reattachment massively; the $\Delta_{\mathrm{llm}}$ variants place the
reattachment and the peak negative wall stress, and $N=4$ removes most of the
remaining profile discrepancies (§3.2, Figs. 19–22). On the NACA 0012 the
hybrids give $C_L/C_D$ of 1.144/1.169 (DDES($\Delta_{\mathrm{llm}}$), $N=3$),
1.168/1.196 ($N=4$) and 1.209/1.235 (IDDES($\Delta_{\mathrm{llm}}$)), against
1.576/1.635 for 2D SA RANS and 0.98/1.06 measured (digitized), and a $C_p$
agreeing with the DES of Shur et al. (§3.3, Table 6, Fig. 24). Mean-flow
perturbations of about 10% in the channels decay back to RANS "almost
instantly", without a figure (§3.1.2). The authors conclude that on fine
grids the high-order DG hybrids behave "more like a wall-modeled ILES rather
than a simple WMLES", and that high order reaches accurate solutions "at a
fraction of the DOFs employed at low order", a statement not quantified
against a low-order code in the paper (§4; see
[implicit LES](/definitions/implicit-les.md) and
[discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)).
They call the self-adjusting LES branch "a dynamic Smagorinsky model";
the paper uses no test filter or Germano identity
(§3.1.2; see the [dynamic procedure](/methods/dynamic-procedure.md)).

## $k$-$\tau$ SST-DDES in a spectral-element solver

Kumar et al. (2025) build the DDES that Tomboulides et al. (2025, §4) had
listed as future work: an SST form of the [$k$-$\tau$ model](/methods/k-tau-model.md)
($\tau_t=1/\omega$, registry §11) made delayed-detached in
[Nek5000](/software/nek5000.md), which they state is, "to the best of our
knowledge", the first DDES in a [spectral element](/methods/spectral-element-method.md)
solver based on the $k$-$\tau$ model
([Kumar et al. (2025)](/sources/kumar-2025.md), §1, §2.2, Eqs. 20–28).
Only the $k$ equation changes; its destruction becomes
$\rho k^{3/2}/l_{\mathrm{DDES}}$ with the $l_{\mathrm{DDES}}$ of Carlsson et al.
above and

$$l_{\mathrm{RANS}}=\frac{\sqrt k\,\tau_t}{C_\mu},\qquad l_{\mathrm{LES}}=C_{\mathrm{DES}}\frac{h_{\max}}{N},\qquad C_{\mathrm{DES}}=0.78F_1+0.61(1-F_1),$$

$h_{\max}$ the longest edge of the spectral element and $N$ the polynomial
degree, $C_\mu=0.09$, $\kappa=0.41$, $a_1=0.31$, and the shielding
function $f_d=1-\tanh\big[(C_{d1}r_d)^{C_{d2}}\big]$, $C_{d1}=20$,
$C_{d2}=3$, $r_d=(\nu_t+\nu)/\big(\kappa^2d^2\sqrt{\tfrac12(S^2+\Omega^2)}\big)$
with $S$, $\Omega$ the strain and vorticity magnitudes (normalization not
printed; Eqs. 25–28). The $\tau_t$ equation is untouched. Delassaux et al.
and Mozaffari et al. (2024) (above) print the same $C_{\mathrm{DES}}$ blend and
$C_{d1}$, $C_{d2}$, Mozaffari et al. the same $r_d$; Delassaux et al. print
$l_{\mathrm{RANS}}=\sqrt k/(\beta^*\omega)$, where Kumar et al. print $C_\mu$ in the
denominator and no value of $\beta^*$ anywhere (§2.1–§2.2).
The authors cite Strelets (2001) for $f_d$, Menter, Kuntz & Langtry (2003)
for the SST-DDES $k$ equation, and Spalart et al. (2006) for grid-induced
separation (§2.2). The appendix gives the same DDES on the
[$k$-$\omega$ SST model](/methods/k-omega-sst-model.md), with
$l_{\mathrm{RANS}}=\sqrt k/(C_\mu\omega)$ and $h_{\max}$ "the maximum edge length
of the cell" (App. A.6, Eqs. A32–A40). Time integration is the
semi-implicit BDF3/EXT3 splitting with characteristics-based steps at a CFL
number of 3.0 (§2.2).

Kumar et al. divide the element edge by $N$ in a $C^0$ nodal
spectral-element method; Alberti et al. (2025), in modal DG, found
$s_\Delta=N+1$ to perform best and $s_\Delta=N$ to move the solution too fast
toward RANS at low and moderate degree (above).

**Evidence** (Kumar et al. 2025, §4):

- **Averaging time.** On the NACA 0021 at $60^\circ$ and $Re=2.7\times10^5$
  with a one-chord span (0.8M degrees of freedom, $N=7$), the running mean
  of $C_L$ needs about 600 convective time units $c/U_\infty$ to settle within
  0.2% of the mean, "about one-third" of the time quoted by Garbaruk et al.
  for a fully implicit low-order code; the relaxed $\pm2\%$ criterion is met
  in the first 100–150 units. The authors could not compare directly, since
  it is unclear whether Garbaruk et al. discarded the transient, and adopt
  at least 200 units on four-chord spans with a stated $\pm2\%$ error
  (§4.2, Fig. 7b).
- **Span.** With a four-chord span (2.9M degrees of freedom) they obtain
  $C_L=0.89$, $C_D=1.48$ against $C_L=1.0$, $C_D=1.76$ on one chord, 0.93
  and 1.51 measured by Swalwell et al., and 0.88 and 1.38 from the SA-DES of
  Garbaruk et al. on four chords; the shedding Strouhal number on the
  projected chord is about 0.19 in all datasets. They attribute the 7% drag
  difference to sampling: the $C_D$ histogram is skewed to large values, and
  their mean step $\Delta t\approx7\times10^{-5}$ gives about 8.5 million samples
  against about 75 000 at $\Delta t=0.02$ in the reference (§4.2, Fig. 7).
- **Grid convergence.** On the [NACA 0012](/benchmarks/naca-0012-airfoil.md)
  at $Re_c=2\times10^6$ and $5^\circ$–$90^\circ$ (four-chord span, Coarse 0.8M,
  Medium 2.6M, Fine 6.5M degrees of freedom, $N=7$, first node at
  $1.2\times10^{-5}c$), Coarse, Medium and Fine differ minimally, so the DDES is
  grid-converged at the Coarse level, whereas the second-order
  finite-volume IDDES of Bidadi et al. converged at the Medium level; the
  authors credit the high-order convergence of the spectral-element method
  (§4.3.2, §5, Fig. 11). The converged loads agree with Bidadi et al. at all
  angles; the DES of Strelets ($Re_c=10^5$, one-chord span) lies higher
  post-stall, which they attribute to the lower Reynolds number and the
  narrower span; post-stall drag falls increasingly below the wall-corrected
  experiments, by about 11% at $90^\circ$ (§4.3.2). The authors write that
  Shur et al.'s justification of post-stall NACA 0012 computations at
  $Re=10^5$ by Reynolds-number insensitivity "is not supported" by Bidadi et
  al., who found about 10% under-prediction of $C_L$ and $C_D$ at a ten
  times higher Reynolds number (§1).
- **Element-interface artefacts.** $Q$-criterion fluctuations at element
  interfaces come from the $C^0$ continuity of the method; a gradient-jump
  penalty at $45^\circ$ on the Fine grid removes them with nearly identical
  $C_L$ and $C_D$ histories, a "merely a cosmetic issue" in the authors'
  words, with results not shown in figures (§4.3.1; see
  [jump-penalty stabilization](/methods/jump-penalty-stabilization.md)).
- **Wind-tunnel confinement.** At $90^\circ$ a DDES inside the tunnel
  cross-section of Critzos et al. ($15c\times6c$, 10.4M degrees of freedom,
  tunnel walls under-resolved at $y^+\sim O(10)$) gives a $C_D$ up to about 13%
  above the unconfined DDES at $Re_c=2\times10^6$ and within 5% of the raw
  (uncorrected) measurement, while the unconfined result differs from the
  corrected measurement by about 11%; the authors call for a reassessment of
  wind-tunnel wall corrections (§4.4.2, §5, Fig. 14).

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
- **Concentrated vortex flows**, as surveyed by Luckring & Rizzi (2024).
  The survey prints the SA form $d_1=\min(d,C_{\mathrm{DES}}\Delta)$ with
  "only one additional model constant ($C_{\mathrm{DES}}=0.65$)", RANS mode
  in stretched boundary-layer cells where $d<\Delta$ and Smagorinsky-like LES
  mode where $d>\Delta$, isotropic LES cells giving the smallest $\Delta$ for a
  given volume, and describes DDES shielding and the IDDES length "depressed
  near the wall" (§2.4.1.4). From the studies it reviews: on the F-15E at
  $65^\circ$ hybrid RANS/LES resolved the unsteady separated flow that URANS
  missed (Forsythe et al.); Morton's SA-based DES with adaptive refinement
  gave the most promising vortex-breakdown predictions of the AVT-080 70°
  delta wing; ZDES was run on the AVT-183 diamond wing, and DDES on the
  CAWAPI F-16XL, whose hybrid pressure bands bracket the flight data, and on
  a chined fighter (§3.1.1.2, §3.1.2.1, §3.2.3.3, §4.1.2; see
  [delta-wing vortex flow](/benchmarks/delta-wing-vortex-flow.md) and
  [mesh adaptation](/methods/mesh-adaptation.md))
  ([Luckring & Rizzi (2024)](/sources/luckring-2024.md)).
- **Ahmed body, as listed by Wang et al. (2024d).** In their drag table the
  DES and IDDES of Guilmineau et al. give total drag coefficients of 0.316
  and 0.346 against 0.279 measured (Table I, as cited; the row is printed
  "IDES", the text says IDDES), beside the authors' wall-modelled LES on
  immersed boundaries ([Wang et al. (2024d)](/sources/wang-2024-k.md); see
  [Ahmed body](/benchmarks/ahmed-body.md) and
  [immersed boundary methods](/methods/immersed-boundary-method.md)).
- **Cited deficiencies and engineering use.** Wu et al. (2024b) cite
  modelled-stress depletion, grid-induced separation and log-layer mismatch
  as the DES limitations that SATES is meant to avoid
  ([Wu et al. (2024b)](/sources/wu-2024-b.md), §I; see
  [SATES](/methods/self-adaptive-turbulence-eddy-simulation.md)); Le et al.
  (2024) call DES and RANS the engineering research hotspot, DNS and LES
  being too costly for engineering use, as they state
  ([Le et al. (2024)](/sources/le-2024.md), §3).
- **Against wall-modelled LES.** Gao et al. (2025) set aside wall-resolved
  LES and DDES for their high-order aeroacoustic solver because both still
  need $y^+\approx1$ at the wall, and state that their slip-wall WMLES,
  whose mean velocity follows the log law for first-point placements
  $y^+=55$–220 in channel flow at $Re_\tau\approx2000$, circumvents the
  log-layer mismatch "that typically plagues conventional detached eddy
  simulation (DES) and WMLES approaches"; they run no DES
  ([Gao et al. (2025)](/sources/gao-2025.md), §I, §III.A.1, Fig. 5; see
  [slip-wall models](/methods/slip-wall-model.md) and
  [log-layer mismatch](/definitions/log-layer-mismatch.md)).

## Qualifications

- Spalart et al. (2006) number the equations of their §4.2 as
  (4.3.1)–(4.3.4); there is no §4.3. Fig. 12a labels its horizontal axis
  "$\nu/\nu$", while Fig. 12b and the text use $\nu_t/\nu$. §1 says that
  $\delta$ "can reach 10% of the airfoil chord" (citing a LESFOIL study),
  while §3.4 reports about 7% for its own airfoil case.

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

- Guo & Wang (2025) print the resolvable filter width as
  $3\max\{\lvert\boldsymbol u\rvert\delta t,\Delta^{1/3}\}$ (Eq. 11): $\lvert\boldsymbol u\rvert\delta t$
  is a length, and $\Delta^{1/3}$ is one only if $\Delta$ is a cell volume,
  while $\Delta$ is a grid length elsewhere in the paper *(compiler check,
  not in the sources)*. Their Fig. 1 writes the switch as
  "$\mu_t/\mu_\infty=0.2$" where Eq. 15 has "$<0.2$", and labels the filtered
  branch with the class name of the unfiltered one. They call the
  $C_D^{\mathrm{rms}}=0.17$ of one variant "slightly lower than the
  experimental and DNS ranges", while their Table 4 lists a DNS range of
  0.117–0.181 that contains it, and they cite an LES/DES range of 0.18–0.22
  where Table 4 lists Rodi's LES range as 0.14–0.27. They judge the
  models partly by how close single-point velocity PDFs in the wake come to
  a Gaussian, and show no reference PDF (§3.1, Figs. 17–20).
- Alberti et al. (2025) print 985 cells for the $11\times17\times5$ mesh
  (Table 3), while $11\times17\times5=935$ and their Table 5 DOF count, 32 725,
  equals $935\times35$ *(compiler check, not in the sources)*; their Table 1
  prints $(N+1)/N_{\mathrm{dof}}^{1/3}$ as 1.40 and 1.48 at $N=2$ and 3, where
  $3/10^{1/3}=1.392$ and $4/20^{1/3}=1.474$ *(compiler check, not in the
  sources)*. Their channel stretching law (Eq. 24) with the base printed as
  $(b+1)(b-1)$ maps $h=0$ to $y=0.927$ for their $a=0.5$, $b=1.05$, not to
  the wall *(compiler check, not in the sources)*. They write "cubic
  square" for the cube root of the cell volume and "$f_D$" for $f_d$, and
  do not print the IDDES constant $C_w$.
- Wang et al. (2024c) do not state explicitly that their a posteriori run
  uses the shielded length (Eq. 40), nor which $\Delta$ their SA-DDES uses.
- Luckring & Rizzi (2024) report the vortex-flow statements above from
  the studies they cite.
- Alberti et al. (2026) state in §3.2 that with $C_{\mathrm{BC}2}=50$ the
  separation on the sphere is anticipated "down to $\phi\approx105°$", while
  their Table 5 lists transition and separation at $99^\circ$ for that
  variant at $N=3$; the Table 5 row "IDDES$_{TRA}$ ($\chi_2=50$)" does not say
  which shielding function it uses, whereas Table 3 writes it with the
  modified one. The NACA 0012 time step is printed as
  $\Delta t=4\times10^{-3}$ without units. The sphere's transition location
  rests partly on the calibrated free-stream eddy-viscosity ratio (§3.2).
- Wu et al. (2026) test AIDDES on two cases (base flow and 30P30N) and a
  flat plate; the ratio $l_{\mathrm{IDDES}}/l_{\mathrm{RANS}}$ of Eq. (21)
  is an indicator they define, not part of the IDDES formulation of
  Gritskevich et al. that they print (Eqs. 17–19). Their measured
  recirculation length, $2.63R$, and the measured reattachment at
  $x/R=2.67$ that Carlsson et al. (2023) use (Applications above) are both
  attributed to Herrin & Dutton; the disagreement is recorded, open, on the
  [supersonic axisymmetric base flow](/benchmarks/supersonic-axisymmetric-base-flow.md)
  page.

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
- [Guo & Wang (2025)](/sources/guo-2025.md) — §1 (groups of DES improvements, $C_{d1}$ recalibrations, as cited); §2.1, Eqs. (6)–(15), Fig. 1 (SST-DDES, filtered eddy viscosity, adaptive grid scale, OpenFOAM classes); §2.2, §3.1–§3.2, Table 4, Figs. 10–25 (square cylinder and periodic hill).
- [Alberti et al. (2025)](/sources/alberti-2025-b.md) — §1–§2, Eqs. (1)–(25), Fig. 1, Table 1 (SA-DDES and SA-IDDES in modal DG, lengths, normalization, equivalent hexahedron); §3.1–§3.3, Tables 3–6, Figs. 2–26 (channels, backward-facing step, NACA 0012); §4.
- [Wang et al. (2024c)](/sources/wang-2024-j.md) — §III.B, Fig. 1 (log-layer mismatch of SA-DES and SA-DDES); §III.F, Eqs. (29), (37)–(40), Figs. 15–16 (interfaces, shielded von Kármán length).
- [Luckring & Rizzi (2024)](/sources/luckring-2024.md) — §2.4.1.4 (DES, DDES, IDDES described; F-15E, as cited); §3.1.1.2, §3.1.2.1, §3.2.3.3, §4.1.2 (vortex-flow applications, as cited).
- [Wang et al. (2024d)](/sources/wang-2024-k.md) — Table I (Ahmed-body drag of cited DES and IDDES).
- [Wu et al. (2024b)](/sources/wu-2024-b.md) — §I (DES deficiencies cited).
- [Le et al. (2024)](/sources/le-2024.md) — §3 (DES and RANS in engineering use).
- [Kumar et al. (2025)](/sources/kumar-2025.md) — §1 (first $k$-$\tau$ DDES in a spectral element code; Shur et al. and Bidadi et al.); §2.2, Eqs. (20)–(28), App. A.6, Eqs. (A32)–(A40) ($k$-$\tau$ SST-DDES and $k$-$\omega$ SST-DDES, $h_{\max}/N$); §4.2, Fig. 7 (NACA 0021, averaging time, span); §4.3, Figs. 10–11 (NACA 0012 grid convergence, gradient-jump penalty); §4.4.2, Fig. 14 (confined DDES); §5.
- [Gao et al. (2025)](/sources/gao-2025.md) — §I (DDES needs $y^+\approx1$); §III.A.1, Fig. 5 (log-layer mismatch of DES, as stated).
- [Wu et al. (2026)](/sources/wu-2026-b.md) — §1 (IDDES delayed transition); §2.3, Eqs. (17)–(21) (SST-IDDES as printed, AIDDES, length-ratio indicator); §2.4, Fig. 1 (flat plate); §4.1.2–§4.1.3, Table 3, Figs. 8, 11 (base flow); §4.2.2–§4.2.3, Figs. 13–14 (30P30N); §5.
- [Alberti et al. (2026)](/sources/alberti-2026.md) — §1 (DES-like models and transition); §2.1, Eqs. (1)–(5) (SA-IDDES in modal DG); §2.1.1, Eqs. (6)–(9) (SA-BCM coupling, modified shielding, $\chi_2$ recalibration); §3.1, Table 3 (Eppler 387); §3.2, Tables 1, 5, Fig. 11 (sphere); §3.3, Table 7, Eq. (14), Fig. 16 (NACA 0012, equivalent Smagorinsky constant); §4.
- [Spalart et al. (2006)](/sources/spalart-2006.md) — §1, Fig. 1 (DES97, grid types, modeled-stress depletion, earlier remedies); §2.1–2.2, Eqs. (2.1)–(2.3) (DDES); §3, Figs. 2–11 (tests); §4.2, Eqs. (4.3.1)–(4.3.4), Fig. 12, footnote 1 (low-Reynolds-number correction $\Psi$, $k$-$\omega$ host); §5 (the founding paper of DDES).
