---
type: Definition
title: "Skin-friction decomposition"
description: "Integral identities that split the mean skin friction of a wall-bounded flow into viscous-dissipation, turbulence-production, pressure-gradient and spatial-growth contributions; the compressible Renard–Deck form, its canonical/mixing-layer split downstream of a shock interaction, and the bound on the growth term."
status: established
aliases: [Renard–Deck decomposition, RD decomposition, mean-kinetic-energy decomposition of skin friction, skin-friction budget]
tags: [boundary-layer, compressible, dns, separated-flow]
timestamp: 2026-10-28T02:18:00Z
---

# Skin-friction decomposition

A skin-friction decomposition writes the mean skin-friction coefficient
$C_f$ of a wall-bounded flow as a sum of wall-normal integrals of mean-flow
and Reynolds-stress quantities, so that the part of the wall drag due to
viscous dissipation, to turbulence production, to the pressure gradient and
to the streamwise growth of the layer can be read separately. The form used
in this bundle is the **Renard–Deck (RD) decomposition**, a balance of mean
kinetic energy in a frame moving with the boundary-layer edge velocity, in
the compressible form that [Yu et al. (2023)](/sources/yu-2023.md) (§4.2)
take from Fan, Li & Pirozzoli (2019) and attribute to Renard & Deck (2016).
Yu et al. (2023) apply it to the recovery region of an oblique
[shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
and split each term into a canonical
[turbulent-boundary-layer](/benchmarks/turbulent-boundary-layer.md) part and
a residue induced by the mixing layer the separation bubble leaves behind.

## Notation (page-local)

Write $U=\langle u\rangle_\rho$, $V=\langle v\rangle_\rho$ for the Favre-averaged
streamwise and wall-normal velocity, $\langle\rho\rangle$, $\langle p\rangle$
for the mean density and pressure, and $\rho_\delta$, $U_\delta$ for their values
at the edge $y=\delta$ ($\delta_{99}$). Let $\tau^{\mathrm{sh}}_v$ be the mean viscous shear
stress, $\tau^{\mathrm{sh}}_t=-\langle\rho u''v''\rangle$ the Reynolds shear stress (positive in
a boundary layer), $\tau^{\mathrm{sh}}=\tau^{\mathrm{sh}}_v+\tau^{\mathrm{sh}}_t$ the total shear stress (the symbols of the
[Yu et al. (2023)](/sources/yu-2023.md) Source page; $T$ stays the temperature), and $\tau^{\mathrm n}_{xx}$ the sum of
the mean viscous and Reynolds streamwise normal stresses (Yu et al.'s
$\bar\tau_{v,xx}+\bar\tau_{t,xx}$). $C_V$, $C_T$, $C_P$, $C_G$ name the four
contributions; a superscript $+$ is wall scaling with $\tau_w$ and $\delta_\nu$.

## The compressible Renard–Deck identity

[Yu et al. (2023)](/sources/yu-2023.md), Eq. (4.4), print

$$\begin{aligned}
C_f&=\underbrace{\frac{2}{\rho_\delta U_\delta^3}\int_0^\delta \tau^{\mathrm{sh}}_v\,\frac{\partial U}{\partial y}\,\mathrm dy}_{C_V}
+\underbrace{\frac{2}{\rho_\delta U_\delta^3}\int_0^\delta \tau^{\mathrm{sh}}_t\,\frac{\partial U}{\partial y}\,\mathrm dy}_{C_T}
+\underbrace{\frac{2}{\rho_\delta U_\delta^3}\int_0^\delta (U-U_\delta)\,\frac{\partial\langle p\rangle}{\partial x}\,\mathrm dy}_{C_P}\\
&\quad+\underbrace{\frac{2}{\rho_\delta U_\delta^3}\int_0^\delta (U-U_\delta)\left[\langle\rho\rangle\left(U\frac{\partial U}{\partial x}+V\frac{\partial U}{\partial y}\right)-\frac{\partial \tau^{\mathrm n}_{xx}}{\partial x}\right]\mathrm dy}_{C_G}.
\end{aligned}$$

The four terms have a direct energetic reading (§4.2): $C_V$ is the direct
viscous dissipation of mean kinetic energy, $C_T$ the production of turbulent
kinetic energy ($\tau^{\mathrm{sh}}_t\,\partial U/\partial y$ is the shear production), $C_P$
the mean pressure-gradient term, and $C_G$ the mean advection,
i.e. the spatial growth of the layer. Their sum is the mean power the wall
supplies to the fluid in the frame convected at $U_\delta$, which goes into
internal energy, turbulent kinetic energy and boundary-layer growth. In wall
units the first three terms become, Eqs. (4.5)–(4.7),

$$\frac{C_V}{C_f}=\int_0^{\delta^+}\frac{u_\tau}{U_\delta}\,\tau^{\mathrm{sh}+}_v\,\frac{\partial U^+}{\partial y^+}\,\mathrm dy^+,\qquad
\frac{C_T}{C_f}=\int_0^{\delta^+}\frac{u_\tau}{U_\delta}\,\tau^{\mathrm{sh}+}_t\,\frac{\partial U^+}{\partial y^+}\,\mathrm dy^+,\qquad
\frac{C_G}{C_f}=\int_0^{\delta^+}\left(\frac{U}{U_\delta}-1\right)\frac{\partial \tau^{\mathrm{sh}+}}{\partial y^+}\,\mathrm dy^+ ,$$

with $\delta^+=\delta/\delta_\nu$; Yu et al. call the formula they use "the
RD formula for zero-pressure-gradient boundary layers" (§4.2).

**Bound on the growth term.** Yu et al. (2023, §4.2), who attribute the
energetic reading of the formula to Renard & Deck (2016), state that "it can
be proved" that $0\le C_G/C_f\le1$ when the turbulent kinetic energy
production is non-negative and the total shear stress is non-increasing;
no proof and no separate citation for the bound are printed. A negative $C_G$ means a
loss (entrainment) of mean kinetic energy in the convective frame.

**Mean-kinetic-energy deficit.** The same section prints the identity (4.10)
$\tfrac12\rho U_\delta^3(\delta^*+\delta^{**})=\tfrac12\left(\rho U_\delta^3\delta-\int_0^\delta\rho U^3\,\mathrm dy\right)$,
with $\delta^{**}$ (page-local) the kinetic-energy thickness and $\rho$
printed without an edge subscript, used to show
where mean kinetic energy goes when the layer thickens.

## Canonical and mixing-layer parts

Downstream of a separated interaction [Yu et al. (2023)](/sources/yu-2023.md)
(§4.1–4.2) construct a canonical mean velocity $U_c$ from a composite
[law of the wall](/definitions/law-of-the-wall.md) (Eq. 4.1, the reference
station's buffer layer below $y^+=30$, $2.55\ln y^++5$ above, and a cosine
wake term in $0.3<y/\delta<1$, all in van Driest-transformed form,
[compressible velocity transformations](/definitions/compressible-velocity-transformation.md))
and define the mixing-layer defect $U_m=U_c-U$. The shear stress is split
the same way, $\tau^{\mathrm{sh}}=\tau^{\mathrm{sh}}_{\mathrm c}+\tau^{\mathrm{sh}}_{v,\mathrm m}+\tau^{\mathrm{sh}}_{t,\mathrm m}$ with $\tau^{\mathrm{sh}}_{\mathrm c}$ the reference-station total
stress as a function of $y/\delta$ (self-similarity of flat-plate layers,
Eqs. 4.2–4.3). Each RD term then splits into a canonical part and a remainder,

$$\frac{C_{Vc}}{C_f}=\int_0^{\delta^+}\frac{u_\tau}{U_\delta}\,\tau^{\mathrm{sh}+}_{v,\mathrm c}\,\frac{\partial U^+_c}{\partial y^+}\,\mathrm dy^+,\quad C_{Vm}=C_V-C_{Vc};\qquad
\frac{C_{Tc}}{C_f}=\int_0^{\delta^+}\frac{u_\tau}{U_\delta}\,\tau^{\mathrm{sh}+}_{t,\mathrm c}\,\frac{\partial U^+_c}{\partial y^+}\,\mathrm dy^+,\quad C_{Tm}=C_T-C_{Tc}$$

(Eqs. 4.8–4.9). The remainders $C_{Vm}$, $C_{Tm}$ therefore contain the cross
products of canonical stress and mixing-layer shear and vice versa, not only
the mixing-layer self-interaction.

## Results in the recovery of a shock interaction

On the DNS of an oblique shock (wedge 8°, shock angle 33.2°) impinging on a
Mach 2.28 boundary layer with mild separation, the database of
[Yu et al. (2022)](/sources/yu-2022-e.md) computed with
[STREAmS](/software/streams.md), [Yu et al. (2023)](/sources/yu-2023.md)
(§4.2, Fig. 10) report:

- outside the interaction zone $(C_V+C_T+C_G)/C_f>0.997$, so the
  zero-pressure-gradient identity is valid there; $C_P$ matters only inside
  the interaction;
- upstream, $C_V$ and $C_T$ each give about 50% of $C_f$ and $C_G$ less than
  10%;
- downstream, $C_V$ is about 40% of $C_f$ with $C_{Vc}\approx C_V$; $C_T$
  exceeds $C_f$ itself while its canonical part $C_{Tc}$ stays near 50%, as
  upstream; the excess $C_{Tm}$ is balanced mostly by a **negative** $C_G$;
- $(C_{Vm}+C_{Tm}+C_G)/C_f$ stays below 15% and settles near 11% from
  $x^*\approx10$ onward ($x^*=(x-x_{\mathrm{imp}})/\delta_r$, page-local, with
  $\delta_r$ the reference-station thickness).

They conclude that the strong outer large-scale motions of the hidden mixing
layer make a small ("trivial") net contribution to the skin friction (§4.2,
§7). The negative $C_G$ is consistent with the stated bound: downstream of
the interaction the total shear stress is not non-increasing in $y$
(Fig. 8), so the hypothesis of the bound fails. In the same region $\delta$
grows quickly while the displacement and kinetic-energy thicknesses stay
almost constant, which the authors read as wall-normal redistribution of
mean kinetic energy by mean convection without significant dissipation
(Eq. 4.10, Fig. 11).

## Qualifications

- The canonical profile behind the split is fitted, not derived: the wake
  coefficient of Eq. (4.1) is linear in $Re_\tau$, with coefficients fitted to
  the profiles at the reference station and at the last station $x_5$, where
  recovery is postulated (§4.1). *(Compiler check, not in the sources: the
  printed fit $0.0005Re_\tau-0.411$ is negative, $-0.31$, at the reference
  $Re_\tau=201$.)*
- The canonical stress of the split is the reference-station total shear
  stress taken as the same function of $y/\delta$ at every station, an
  assumption Yu et al. (2023, §4.2) base on the self-similarity of
  flat-plate boundary layers (Kumar & Mahesh 2021, as they cite it).
- The bundle's only source for the decomposition is Yu et al. (2023); the
  original derivations (Renard & Deck 2016; Fan, Li & Pirozzoli 2019) are
  cited there, not ingested.

# Citations

- [Yu et al. (2023)](/sources/yu-2023.md) — §4.1, Eq. (4.1); §4.2, Eqs. (4.2)–(4.10), Figs. 8, 10, 11; §7.
- [Yu et al. (2022)](/sources/yu-2022-e.md) — §2 (the DNS database analysed by Yu et al. 2023).
