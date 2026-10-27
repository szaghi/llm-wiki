---
type: Method
title: "Slip-wall models"
description: "Wall-modelled LES boundary conditions that let the filtered velocity slip at the wall instead of imposing a wall stress: the dynamic Robin slip condition of Bose & Moin as reviewed by Bose & Park, and the volume-filtered wall slip of Rickard & Kasbaoui with its van Driest and slip-length closures."
status: established
aliases: [slip wall, dynamic slip wall, dynamic slip-wall model, Robin slip condition, wall-slip model, slip-length model, Van Driest slip model]
tags: [wall-model, wmles, filtering, immersed-boundary]
timestamp: 2026-10-27T15:54:00Z
---

# Slip-wall models

A slip-wall model closes the near-wall region of a
[wall-modelled LES](/methods/wall-modelled-les.md) by prescribing the
*filtered velocity at the wall*, which need not vanish, rather than by
replacing no slip with a modelled wall stress as the
[equilibrium](/methods/equilibrium-wall-model.md) and
[non-equilibrium wall models](/methods/nonequilibrium-wall-model.md) do. The
premise is that the true no-slip condition holds for the unfiltered velocity
but not, in general, for the filtered one once the filter width near the
wall is comparable to the scale of the near-wall gradients. Two families
are in the sources: the dynamic slip wall of Bose & Moin (2014), a Robin
condition derived from a differential filter, reviewed by
[Bose & Park (2018)](/sources/bose-2018.md), and the volume-filtered wall
slip of [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md), derived for
[immersed-boundary](/methods/immersed-boundary-method.md) LES. In both, the
model needs no matching height $h_{\mathrm{wm}}$ and no assumed velocity
profile between the wall and the LES; the slip is the only unclosed wall
quantity and the wall stress follows from it.

Page-local notation: $n$ the wall-normal coordinate pointing into the
fluid; $l_p$ the regularization coefficient of a differential filter (a
length squared); $C\Delta_w$ the slip length of the Robin condition. The
volume-filtering symbols $\Delta_f$, $\varphi_f$, $\boldsymbol\ell$,
$\boldsymbol u_{\mathrm{slip}}$ and the gradient ratio $\boldsymbol\Lambda$
are the shared ones of the registry (§11).

## Why the filtered velocity slips

Bose & Park (2018, §2.3) state that imposing the true (unfiltered) boundary
conditions on filtered fields is valid only when the near-wall filter width
is small against the length scale of the velocity gradients (Ghosal & Moin
1995, as cited), "which is certainly violated in WMLES". Rickard &
Kasbaoui (2026, §2.3) reach the same statement from exact filtering
identities: with a compact kernel of width $\Delta_f$, no slip,
$\boldsymbol u_{\mathrm{slip}}=0$, holds only in the "DNS limit"
$\Delta_f^+<1$. Their a priori filtering of channel DNS at $Re_\tau=5200$
(Lee & Moser, as cited) quantifies the slip that a WMLES-size filter must
carry: the mean streamwise slip is $6.93u_\tau$ at $\Delta_f^+=50$ and
$13.5u_\tau$ at $\Delta_f^+=300$, growing logarithmically with the filter
width, while the wall-normal and spanwise mean slips are negligible; the
streamwise slip fluctuates by about $1.5u_\tau$ at every width and carries
near-wall streaks at $\Delta_f^+=50$ and outer-layer structures at 300 (§3.2,
Figs. 6–7).

## The dynamic slip wall (Bose & Moin)

Bose & Park (2018, §2.3, Eqs. 15–16), reviewing the first author's earlier
work, start from a modified differential filter,

$$\bar\phi-\frac{\partial}{\partial x_k}\left(l_p\frac{\partial\bar\phi}{\partial x_k}\right)=\phi,$$

with $l_p\propto\Delta^2$ in the interior and $l_p=0$ on the boundary. The
filter turns the no-slip condition of $\phi=u_i$ into a Robin condition for
the filtered velocity,

$$\bar u_i-C\Delta_w\frac{\partial\bar u_i}{\partial n}=0\qquad\text{at the wall},$$

whose slip length $C\Delta_w$ is computed by a Germano-like
[dynamic procedure](/methods/dynamic-procedure.md). Its properties as the
review states them:

- **No modelling assumptions on the inner layer.** No velocity profile,
  stress alignment or equilibrium is assumed, and there is no empirical
  coefficient when the slip length is computed dynamically; the model also
  needs no matching height, one of the open problems the review names for
  other wall models (§2.3, §5).
- **Transpiration.** A finite slip admits wall-normal velocity at the wall
  and so a non-zero wall Reynolds stress, which "has been shown to reduce"
  the over-prediction of the near-wall streamwise intensity typical of
  stress-based wall models (§2.3).
- **Limits that recover no slip.** The condition reverts to no slip when
  $C\Delta_w$ is small against the viscous length or at a separation point,
  and in laminar regions the dynamic procedure drives $C\Delta_w\to0$, so
  the model goes laminar without a separate transition sensor (§2.3, §4.1);
  equilibrium-type models instead need such a sensor (see the
  [equilibrium wall model](/methods/equilibrium-wall-model.md)).
- **Relation to stress models.** Yang et al. (2016), as cited, showed that
  its wall stress can be equivalent to that of an equilibrium wall-stress
  model and functionally similar to virtual-wall conditions (§2.3).
- **Weak points.** Its accuracy is limited by the robustness of the dynamic
  procedure, which is sensitive to the SGS model and the numerics, and
  compressible and heat-transfer forms remain open (§2.3).

[Lv et al. (2021)](/sources/lv-2021.md) (§II B 1) call the slip wall "the
first attempt" to remove the "RANS legacies" of wall modelling, the separate
wall-model solver with its own equations, but add that it "has numerical
difficulty in some codes"; their own route is a reconstruction basis
containing the log law (see [non-equilibrium wall models](/methods/nonequilibrium-wall-model.md)).

### Applications cited

All results here are cited by the review, which runs no simulation. On the
[NACA 4412](/benchmarks/naca-4412-airfoil.md) near stall
($Re_c=1.6\times10^6$) equilibrium, non-equilibrium and dynamic slip-wall
models all reproduce the trailing-edge pressure plateau; on the
[periodic hill](/benchmarks/periodic-hill.md) ($Re_h=10\,595$) slip,
equilibrium and non-equilibrium models agree favourably with DNS, the
differences "may be due more to" the outer-LES numerics; and a car side
mirror at $Re_L\sim7\times10^6$ was computed with the slip wall (Bose &
Park 2018, §4.3). [Mukha et al. (2025)](/sources/mukha-2025.md) (§IV.B),
comparing their own flat-plate WMLES with published ones, cite a
dynamic-slip result "well within" 4 % in $C_f$. Several sources cite the
dynamic slip wall of Bose & Moin (2014) and its later version by Bae et al.
(2019) among the WMLES options without formulating it
([Fowler et al. 2022](/sources/fowler-2022.md), §1;
[Vadrot et al. 2023b](/sources/vadrot-2023-b.md), §I;
[Bae & Koumoutsakos 2022](/sources/bae-2022.md), Introduction, who list
it as "coefficient-free"). Fowler et al. (§1) add a doubt: "at
increasing Reynolds numbers, it is unclear that such modelling can
accurately capture subtle Reynolds number dependencies of the predicted
friction drag".

## The volume-filtered wall slip (Rickard & Kasbaoui)

Rickard & Kasbaoui (2026, §2) filter the incompressible equations with a
compact, symmetric kernel of support $\Delta_f$ that is truncated by the
fluid indicator and, unlike the filter of Bose & Moin as they describe it,
*not rescaled* near the wall: the deficit is carried by the fluid volume
fraction $\varphi_f$, which is $1/2$ at a planar wall, and filtered
quantities extend $\Delta_f/2$ into the solid (§2.1). Exact commutation
identities (after Dave et al. 2023, as cited) turn the wall terms into an
immersed-boundary body force and leave, besides the SGS stress, a closed
residual viscous stress that is linear in the slip at the wall (§2.2–2.3,
Eqs. 2.17–2.27). The only unclosed wall quantity is the slip
$\boldsymbol u_{\mathrm{slip}}=\bar{\boldsymbol u}|_w-\boldsymbol u_w$, and
the wall stress follows from it (Eq. 2.25), so "modelling the wall slip is
in essence a turbulence wall model" (§2.3). They name the resulting method
immersed boundary-modelled LES.

Two closures are calibrated a priori on the filtered channel DNS (§4–5):

- **Van Driest slip model** (§4.1, Eqs. 4.1–4.5). The van Driest mean
  profile ($\kappa=0.41$, $A^+=26$; see the
  [law of the wall](/definitions/law-of-the-wall.md)) is volume-filtered to
  give the mean slip, and for $\Delta_f^+\gg1$ the result is fitted as

  $$\frac{\langle u_{\mathrm{slip}}\rangle}{u_\tau}=\frac1{\varphi_{f,w}}\left[\frac1{2\kappa}\ln\frac{\Delta_f^+}2+a_0+b_0\left(\Delta_f^+\right)^{-n_0}\right],$$

  with $\varphi_{f,w}$ the wall value of $\varphi_f$ and $a_0$, $b_0$, $n_0$
  fit constants (page-local; across four kernels $a_0=0.81\pm0.21$,
  $b_0=-67.5\pm4.5$, $n_0=0.92\pm0.03$, §5, Table 1). The exact filtered
  profile agrees with the filtered DNS over $\Delta_f^+=50$–300, and the fit
  is within 1 % of it for $\Delta_f^+\ge100$ and diverges as
  $\Delta_f^+\to0$ (Fig. 11).
- **Slip-length model** (§4.2, Eqs. 4.13–4.27). The commutation identity
  gives a Robin condition of the Bose & Moin type,
  $\boldsymbol u_{\mathrm{slip}}=\mathrm{diag}(\boldsymbol\ell)\,\partial\bar{\boldsymbol u}/\partial n|_w$,
  with slip lengths fixed by the filter itself,

  $$\boldsymbol\ell=\frac{\varphi_{f,w}\,(\boldsymbol\Lambda-1)}{(\partial\varphi_f/\partial n)|_w},$$

  where $\boldsymbol\Lambda$ is the ratio of the mean filtered wall gradient
  to the mean gradient of the filtered velocity. Since
  $\boldsymbol\Lambda\to1$ and $\boldsymbol\ell\to0$ as $\Delta_f\to0$, the
  model recovers no slip in the DNS limit (Eq. 4.24). Fitted on joint PDFs
  of the two gradients, $\Lambda_x=1+0.251\,(\Delta_f^+)^{0.5385}$ and
  $\ell_x^+=0.0798\,(\Delta_f^+)^{1.5385}$ for the cosine kernel, roughly
  $\ell_x^+\approx0.08\,(\Delta_f^+)^{1.5}$ for all four kernels tested;
  $\Lambda_y=\Lambda_z=1$ reproduces the negligible wall-normal and spanwise
  slip of the channel (Eqs. 4.25–4.27, 7.3). The authors stress that this
  derivation holds for curved walls (curvature resolved by $\Delta_f$) and
  moving walls, which they say the Taylor-series argument of Bose & Moin
  does not cover (§4.2).

A dynamic version, which sets the slip length from the Germano identity
between two filter levels with the fitted scaling
$\hat\ell=(\hat\Delta_f/\Delta_f)^{n_1+1}\ell$ ($n_1\approx0.53$; hat the
test filter), one length per direction and an explicit positive root rather
than a least-squares fit, is derived but not tested (§6, Eqs. 6.9, 7.4).
Existing SGS models such as dynamic Smagorinsky are expected to close the
SGS stress (§7).

## Slip against stress: how the wall condition enters

The two families agree that the slip, not the stress, is the primitive
quantity, and they share the Robin form; they differ in where it comes
from. In Bose & Moin's model, as Bose & Park present it, the slip length
is a free coefficient made dynamic; in Rickard & Kasbaoui's, the slip length
is an exact function of the filter and of a gradient ratio, and only
$\boldsymbol\Lambda$ has to be modelled. Neither source runs a posteriori
WMLES with the volume-filtered closures, so the two have not been compared
on a common flow in the bundle.

Wall-stress models take the other route. [Van Noordt et al. (2022)](/sources/vannoordt-2022.md)
(§2.6) contrast their immersed-boundary WMLES with Bose & Moin's dynamic
slip (Robin) condition and do not use it: the stress and heat flux of an
equilibrium wall model are applied explicitly as viscous fluxes at the
immersed boundary, and the ghost-cell tangential velocity is extrapolated
linearly from two interior sampling points. [De Vanna et al. (2022)](/sources/devanna-2022.md)
(§2.2) keep no slip and impose the modelled stress through an augmented
wall viscosity (see [wall-modelled LES](/methods/wall-modelled-les.md)).

## Qualifications

- The formulation of the dynamic slip wall here is the review's
  (Bose & Park 2018, §2.3); Bose & Moin (2014), Bae et al. (2019) and Yang
  et al. (2016) are not ingested, and the dynamic procedure for $C\Delta_w$
  is not written out in the review.
- Rickard & Kasbaoui's closures rest on one Reynolds number
  ($Re_\tau=5200$); the $Re_\tau$ dependence of $\boldsymbol\Lambda$ is
  "expected" to be secondary, and rough, moving or deforming and strongly
  separated walls are outside the stated scope (§4.2, §7). There are no a
  posteriori runs.
- Rickard & Kasbaoui state in §4.1 that their slip fit is accurate for
  $\Delta_f^+\ge50$, against $\ge100$ in their Fig. 11(b) and Eqs. (5.4),
  (7.1); their Fig. 6 caption puts the streamwise slip fluctuations at
  "approximately 10 % or less" of the mean slip, while $1.5u_\tau$ against
  $6.93u_\tau$ at $\Delta_f^+=50$ is about 22 % *(compiler check, not in the
  sources)*. Further printed items are on their Source page.

# Citations

- [Bose & Park (2018)](/sources/bose-2018.md) — §2.3, Eqs. (15)–(16); §4.1; §4.3; §5.
- [Rickard & Kasbaoui (2026)](/sources/rickard-2026.md) — §2.1–2.3, Eqs. (2.17)–(2.27); §3.2, Figs. 6–7; §4.1–4.2, Eqs. (4.1)–(4.27), Figs. 11–13; §5, Table 1; §6, Eq. (6.9); §7, Eqs. (7.1)–(7.4).
- [Lv et al. (2021)](/sources/lv-2021.md) — §II B 1.
- [Mukha et al. (2025)](/sources/mukha-2025.md) — §IV.B (arXiv v1).
- [Fowler et al. (2022)](/sources/fowler-2022.md) — §1.
- [Vadrot et al. (2023b)](/sources/vadrot-2023-b.md) — §I.
- [Bae & Koumoutsakos (2022)](/sources/bae-2022.md) — Introduction.
- [van Noordt et al. (2022)](/sources/vannoordt-2022.md) — §2.6, Eqs. (41)–(42).
- [De Vanna et al. (2022)](/sources/devanna-2022.md) — §2.2, Eqs. (7a)–(7b).
