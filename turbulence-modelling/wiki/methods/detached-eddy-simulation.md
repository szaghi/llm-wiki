---
type: Method
title: "Detached-eddy simulation and its delayed and zonal forms"
description: "The single-model hybrid RANS/LES in which a RANS model's length scale is capped by a grid length so that the model acts as a subgrid model away from walls; the DES switch and its failure on ambiguous grids, the DDES shielding function, ZDES modes and their grid lengths, and applications."
status: established
aliases: [DES, DDES, delayed detached-eddy simulation, IDDES, improved delayed DES, ZDES, zonal detached-eddy simulation, DDES-SST, ZDES mode 2, ZDES mode 0+1]
tags: [des, hybrid-rans-les, rans, les, turbomachinery, mesh-adaptation]
timestamp: 2026-10-25T19:45:00Z
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
symbols: $d_{\mathrm{DES}}$ the hybrid length, $\Delta_{\max}=\max(\Delta x,\Delta y,\Delta z)$
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
  "RANS-like" (§3.2.1).
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
- None of the three applications prints the DES equations in full;
  Mozaffari et al. print none.

# Citations

- [François et al. (2022)](/sources/francois-2022.md) — §1, §3.1 (pp. 5–6, footnote 2), §3.2.1, §3.4–3.5, §4.1–4.2 Fig. 9, §5.3–5.4 Figs. 12–15.
- [Basile et al. (2023)](/sources/basile-2023.md) — §1, §2.2 Eqs. 5–7, §3.3–3.4, §4.2.2 Fig. 7, §4.2.3 Table 1 Fig. 9.
- [Mozaffari et al. (2022)](/sources/mozaffari-2022.md) — §1 Fig. 1, §2, §4.1, Table 2, §5.
- [Haering et al. (2022)](/sources/haering-2022.md) — §I, §II A, §II C.
- [Abe (2021)](/sources/abe-2021.md) — §IV C–D, Figs. 9–11.
- [Yan et al. (2022)](/sources/yan-2022.md) — §2.3.
- [Goc et al. (2021)](/sources/goc-2021.md) — §1.
