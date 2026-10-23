---
type: Definition
title: "Ducros shock sensor"
description: "The Ducros sensor flags compressions by the share of dilatation in the velocity-gradient magnitude; the page gives the classical squared ratio, the modified compression-only form that switches hybrid central/TENO and central/WENO schemes, its use as a weight blending WENO-Z with a first-order flux, its regularization and thresholds, and its recorded failures and repairs."
status: established
aliases: [Ducros sensor, modified Ducros sensor, improved Ducros sensor, Ducros dilatation–vorticity sensor, Ducros level, dilatation-to-vorticity ratio]
tags: [central-scheme, teno, weno, finite-difference, turbulence]
timestamp: 2026-10-23T05:41:00Z
---

# Ducros shock sensor

The **Ducros sensor** is a pointwise physical shock detector built from the
velocity field alone. It compares the dilatation $\nabla\cdot v$ with the
vorticity $\nabla\times v$: at a shock the dilatation dominates and the
sensor is close to one, in vortical turbulence the vorticity dominates and the
sensor is close to zero. It does not look at the reconstructed data, unlike
the smoothness-based and TENO-flag indicators on
[troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md).
In this bundle it serves two purposes. It switches a low-order dissipation
term in a central scheme with artificial dissipation
([Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md)). It also selects
where a [hybrid scheme](/methods/hybrid-weno.md) leaves its central
energy-preserving flux for WENO-Z or [TENO](/methods/targeted-eno.md)
([De Vanna et al. (2023a)](/sources/devanna-2023.md);
[De Vanna et al. (2023b)](/sources/devanna-2023-b.md);
[De Vanna et al. (2023c)](/sources/devanna-2023-c.md)). In a hypersonic
Cartesian solver it weights a blend of fifth-order WENO-Z with a
first-order flux ([McQuaid & Brehm (2024)](/sources/mcquaid-2024.md)).

## Two forms

Page-local symbols: $\Phi_{\mathrm D}$ is the classical ratio,
$\Psi_{\mathrm D}$ the modified sensor, $\Psi^*$ its threshold and
$\epsilon_{\mathrm D}>0$ the regularization (the same letter as on
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

**Classical squared ratio.** As one factor of their product sensor $\Xi_i$,
Sciacovelli et al. (§3, Eq. (36)) use

$$\Phi_{\mathrm D}=\frac{(\nabla\cdot v)^2}{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}},\qquad\epsilon_{\mathrm D}=10^{-16}.$$

This form is even in the dilatation, so it flags expansions as well as
compressions. It lies in $[0,1)$.

**Modified, compression-only form.** De Vanna et al. (2023a, §3.2, Eq. (9))
call the following a "modified Ducros shock sensor":

$$\Psi_{\mathrm D}=\max\Big(-\frac{\nabla\cdot v}{\sqrt{(\nabla\cdot v)^2+\lvert\nabla\times v\rvert^2+\epsilon_{\mathrm D}}},\ 0\Big),\qquad \epsilon_{\mathrm D}=\Big(\frac{v_\infty}{\delta_0}\Big)^2,$$

with $v_\infty$ the free-stream velocity and $\delta_0$ the inflow
boundary-layer thickness. The URANOS paper prints the same expression as the
"improved Ducros sensor" with $\epsilon_{\mathrm D}=(v_\infty/L)^2$, $L$ a
reference length (De Vanna et al. 2023b, §3.2, Eq. (10)). De Vanna et al.
(2023c, §3.2, Eq. (13)) write it in index notation, with the Levi-Civita
tensor for the vorticity and $\epsilon_{\mathrm D}=\epsilon_0^2$, where
$\epsilon_0=v_\infty/L_0$ is called a "reference velocity gradient". Two
changes separate it from the classical form. Only compressions are flagged,
since the max with zero discards $\nabla\cdot v>0$. The ratio is not squared.
*(Compiler check, not in the sources: with the same $\epsilon_{\mathrm D}$,
$\Psi_{\mathrm D}=\sqrt{\Phi_{\mathrm D}}$ wherever $\nabla\cdot v<0$, and
$\Psi_{\mathrm D}=0$ elsewhere. A threshold $\Psi^*$ on the modified sensor
is therefore the threshold $(\Psi^*)^2$ on the classical ratio: the values
$0.1$, $0.2$, $0.4$ below correspond to $0.01$, $0.04$, $0.16$.)*

**Regularization.** The two groups set $\epsilon_{\mathrm D}$ in opposite
ways. Sciacovelli et al. take a fixed $10^{-16}$. They recall that the
remedy of an earlier work for spurious activation is to parametrize
$\epsilon_{\mathrm D}$ by the flow scales, "at the cost of generality", and
prefer to multiply by two other factors (§3). De Vanna et al. scale
$\epsilon_{\mathrm D}$ with a free-stream velocity gradient, which is that
flow-scale parametrization. *(Compiler check, not in the sources: with
$\epsilon_{\mathrm D}>0$ the sensor stays below one, so a threshold
$\Psi^*=1$ never flags. De Vanna et al. (2023a, §6) call $\Psi^*=1$
"assumable as a pure energy-preserving strategy", which agrees.)*

## Use in hybrid central/TENO schemes

In URANOS the sensor is evaluated at cell faces. Where
$\Psi_{\mathrm D,i+1/2}>\Psi^*$, the face and a band of neighbours use
WENO-Z or TENO, and the sixth-order kinetic-energy-preserving central scheme
of Pirozzoli is used elsewhere
([split convective forms](/methods/split-convective-forms.md)). The band is
2, 3 or 4 cells for orders 3, 5 and 7 (De Vanna et al. 2023a, §3.2;
De Vanna et al. 2023b, §3.2). $\Psi^*=0$ means pure WENO or TENO everywhere.
The paper also offers two other a priori detectors, a density gradient and a
density jump. It recommends the Ducros form for wall flows and states that
$\Psi^*$ "is strongly dependent on the flow" and needs preliminary tuning
(De Vanna et al. 2023b, §3.2, Eqs. (8)–(10)).

**Thresholds measured on wall turbulence.** De Vanna et al. (2023a) run a
parameter study of $\Psi^*$ on wall-modelled LES of spatially developing
boundary layers ([wall-modelled LES](/methods/wall-modeled-les.md);
[supersonic turbulent boundary layer](/benchmarks/supersonic-turbulent-boundary-layer.md);
§§4.3–4.4, Figs. 5–9, Tables 2–4). The flow is nominally shock-free.

- At Mach 2, $\Psi^*=0.1$ already restores realistic wall statistics where
  pure WENO-Z or TENO damp or destroy wall turbulence. With $\Psi^*=0.2$ a
  dependence on the WENO order persists but does not significantly affect
  global accuracy. With $\Psi^*=0.4$ the WENO and TENO profiles collapse onto
  identical curves, because most of the flow is computed by the central
  scheme.
- At Mach 5.86 the pure central scheme diverges, which the authors attribute
  to shocklets. $\Psi^*=0.2$ is "the highest limit that ensures the current
  arrangement's numerical stability" (§4.4), and $\Psi^*\simeq0.2$ is the
  recommended compromise (§6).

The hybrids cost 0.90–1.00 of the pure central scheme per iteration (§4.3.1,
Table 2). The later immersed-boundary work uses $\Psi^*=0.1$ with TENO-A7 and
TENO-A5 (De Vanna et al. 2023c, §§4.3–4.4;
[adaptive TENO](/methods/adaptive-teno.md)).

**Two more switched schemes.** [Duronio & Di Mascio (2024)](/sources/duronio-2024.md)
(§2, Eq. (7)) use the modified form, compression-only and not squared,
with $\epsilon_{\mathrm D}=v_0^2/L_0^2$ from "suitable velocity and
length scales" (values not printed), calling it "the classical shock
sensor" of Ducros et al.; averaged to faces, it switches on the
AUSM$^+$-up dissipation of the convective flux of a
kinetic-energy-preserving central scheme in
[OpenFOAM](/software/openfoam.md) above $\Psi^*=0.05$. The pressure
dissipation is not switched. [Jiao et al. (2024)](/sources/jiao-2024.md)
(App. D) use the classical squared ratio with $\epsilon_{\mathrm D}=10^{-20}$,
combined with gas and vapour volume-fraction variation sensors, to
blend a fourth-order central, an upwind MUSCL and a THINC reconstruction
in an implicit-LES scheme for multiphase flow, with the threshold 0.95
they take from Egerer et al. The form Duronio & Di Mascio call
"classical" is thus not the squared ratio Jiao et al. use.

## Use as a blending weight towards first order

McQuaid & Brehm (§3.8, Eq. (20)) blend, on the block-structured
Cartesian off-body grid of their overset hypersonic solver, the
fifth-order finite-difference [WENO-Z](/methods/weno-z.md) flux
(reconstruction in [characteristic variables](/methods/characteristic-decomposition.md)
on the Roe-averaged state, Steger–Warming flux splitting) with a
first-order flux $\hat f^{\mathrm O1}_{i+1/2}$ (page-local),

$$\hat f_{i+1/2}=(1-\tilde\alpha_{\mathrm D})\,\hat f^{\mathrm{WENO}}_{i+1/2}+\tilde\alpha_{\mathrm D}\,\hat f^{\mathrm O1}_{i+1/2},$$

where $\tilde\alpha_{\mathrm D}$ (page-local) is the "Ducros sensor
value" of the "classical Ducros sensor" they cite; the sensor formula,
its regularization and any threshold are not printed. The scheme thus
falls fully to first order at strong shocks; unlike the hybrid switches
above, the partner of WENO-Z is a first-order flux, not an
energy-preserving central one (see [hybrid central–WENO schemes](/methods/hybrid-weno.md)).
They motivate it by shock-induced artefacts on grids not aligned with
the shock: "even the reduced order WENO scheme can produce pre- and
post-shock artifacts". On the Mach 9.47 Mars Science Laboratory capsule
at $8^\circ$ incidence they compare four Cartesian flux treatments,
WENO-Z with local Rusanov splitting, with stencil-maximum ("global")
Rusanov splitting, with Steger–Warming splitting, and the Ducros blend
(§4.1, Fig. 14). The first three send velocity streaks from the shock
to the interface with the near-body grid, which imprint a significant
artefact in the surface heat flux; only the Ducros blend removes it, at
the cost of a slightly more diffused shock. They assume, without
testing it, that the cause is the misalignment of shock and grid, and
attribute a slight leeward over-prediction of the heating and a
somewhat low peak temperature (AS-202 capsule) to the first-order
reduction (§4.1, §4.3). They describe the sensor as detecting shocks
"with a minimal increase in computational overhead".

## Failure modes and repairs

- **Smooth irrotational flow.** Where both the dilatation and the vorticity are
  small, as outside boundary and mixing layers, the classical ratio can be close
  to one. On an underexpanded jet it is near unity "even in smooth irrotational
  regions" (Sciacovelli et al. 2021, §3, §5.1, Fig. 8(a)).
- **One space dimension.** In 1D the Ducros factor is inactive (Sciacovelli et
  al. 2021, §4.3). *(Compiler check, not in the sources: with
  $\nabla\times v=0$, $\Phi_{\mathrm D}\to1$ wherever
  $(\nabla\cdot v)^2\gg\epsilon_{\mathrm D}$, so the factor does not separate a
  shock from a smooth compression.)*
- **Under-resolved turbulence.** De Vanna et al. (2023a, §3.2, §4.3.3) state
  that grid noise and physical turbulent fluctuations "are often read as shocks"
  by shock detectors in low-resolution settings such as WMLES. De Vanna et al.
  (2023c, §3.2) make the same point for ENO-like detection and call the modified
  Ducros sensor "peculiarly accurate" in such cases, with "minimal intrusion of
  shock-capturing where it is not required". They cite Ducros et al. (1999)
  and their 2023a study for this; the 2023a study varies the threshold of the
  Ducros sensor only and compares it with no other detector.
- **Case dependence.** [Fu (2023)](/sources/fu-2023.md) (§3.4) calls physical
  sensors such as Ducros' case-dependent. Fu presents the TENO-based indicator as
  "more universal" because it separates non-smooth scales in spectral space
  ([hybrid central–WENO schemes](/methods/hybrid-weno.md)). Fu also records that
  the TENO6-A variant used for transitional shock/boundary-layer interaction
  replaces the TENO discontinuity measure by a modified Ducros sensor (§4.1,
  §5.4; [adaptive TENO](/methods/adaptive-teno.md)). [Liang & Fu (2024b)](/sources/liang-2024-b.md)
  (§3.1) make the same claim for their eight-point TENO-type indicator of
  the TENO-S hybrid, which separates non-smooth high-wavenumber
  fluctuations "in the wavenumber space" and is "more universal for
  general conservation laws" than physical-variable sensors such as the
  Ducros sensor; they show indicator maps but no comparison with a
  Ducros-switched run ([targeted ENO](/methods/targeted-eno.md)).

**Repair by multiplication.** Sciacovelli et al. (§3, Eq. (36)) multiply the
classical ratio by the Bhagatwala–Lele dilatation switch and Jameson's
pressure sensor ($\Xi_i$, written out on
[troubled-cell indicators](/definitions/troubled-cell-indicator.md) and
[numerical dissipation](/definitions/numerical-dissipation.md)). On the
underexpanded jet the product confines the low-order dissipation to the
intercepting shocks, the Mach disk and the reflected shocks, with values below
$0.02$ elsewhere (§5.1, Fig. 8).

## Not a Ducros sensor: Jameson-type pressure sensors

The pressure sensor of Jameson et al. that enters Sciacovelli et al.'s
product $\Xi_i$ is a different detector, a normalized second difference
of a scalar rather than a velocity-gradient ratio.
[Berta et al. (2024)](/sources/berta-2024.md) (§3.4, Eq. (35), arXiv v4)
use a Jameson-type sensor of this kind, not the Ducros sensor, in their
fourth-order MHD finite-volume scheme: per direction,
$(\bar q_{i+1}-2\bar q_i+\bar q_{i-1})/(\lvert\bar q_{i+1}\rvert+2\lvert\bar q_i\rvert+\lvert\bar q_{i-1}\rvert+\epsilon)$
on the cell averages $\bar q$ (page-local) of density, pressure and magnetic pressure, the
maximum over them and the Euclidean norm over directions compared with
a threshold whose value is not printed; flagged cells and their first
neighbours drop to a lower-order reconstruction. They note that it
keeps the stencil compact, "albeit three zones may not be sufficient to
distinguish a discontinuity from a smooth extremum", and propose a
derivatives-ratio detector beside it (see
[troubled-cell indicators](/definitions/troubled-cell-indicator.md)).

## Qualifications

- McQuaid & Brehm print neither the Ducros formula nor a threshold, so
  their blend cannot be compared quantitatively with the hybrid
  switches above; it is a continuous weight, not a binary switch.
- Thresholds do not transfer between the two forms. A value of $\Psi^*$ for
  the modified sensor equals $(\Psi^*)^2$ for the classical ratio (compiler
  check above), and both depend on the choice of $\epsilon_{\mathrm D}$. The
  recommended $\Psi^*\simeq0.2$ was obtained on boundary layers at Mach 2 and
  5.86 with $\epsilon_{\mathrm D}=(v_\infty/\delta_0)^2$ (De Vanna et al.
  2023a).
- The sensor is tested as a cell-face value $\Psi_{\mathrm D,i+1/2}$, but
  none of the three De Vanna papers states how the face value is formed from
  the velocity gradients at the grid points.
- De Vanna et al. (2023a, §3.2, Eq. (9)) and De Vanna et al. (2023b,
  Eq. (10)) use the same symbol for the sensor regularization and for the
  WENO-Z regularization $\epsilon=10^{-12}$. The page keeps them apart.

# Citations

- [Sciacovelli et al. (2021)](/sources/sciacovelli-2021.md) — §3, Eq. (36); §4.3; §5.1, Fig. 8: classical Ducros factor, its failures, product sensor (arXiv v1).
- [De Vanna et al. (2023a)](/sources/devanna-2023.md) — §3.2, Eq. (9); §§4.3–4.4, Tables 2–4, Figs. 5–9; §6: modified sensor and threshold study.
- [De Vanna et al. (2023b)](/sources/devanna-2023-b.md) — §3.2, Eqs. (8)–(10): improved Ducros sensor among URANOS detectors, flagged band, tuning.
- [De Vanna et al. (2023c)](/sources/devanna-2023-c.md) — §3.2, Eq. (13); §§4.3–4.4: index form, $\Psi^*=0.1$ with TENO-A.
- [Fu (2023)](/sources/fu-2023.md) — §3.4, §4.1, §5.4: case dependence of physical sensors; modified Ducros sensor in TENO6-A.
- [Duronio & Di Mascio (2024)](/sources/duronio-2024.md) — §2, Eq. (7): modified form switching AUSM$^+$-up dissipation, $\Psi^*=0.05$.
- [Jiao et al. (2024)](/sources/jiao-2024.md) — App. D: classical ratio in a multiphase implicit-LES blending sensor.
- [McQuaid & Brehm (2024)](/sources/mcquaid-2024.md) — §3.8, Eq. (20); §4.1, Fig. 14; §4.3: Ducros-weighted blend of WENO-Z with a first-order flux, heating artefacts on non-aligned grids.
- [Liang & Fu (2024b)](/sources/liang-2024-b.md) — §3.1: TENO-type indicator claimed more universal than the Ducros sensor.
- [Berta et al. (2024)](/sources/berta-2024.md) — §3.4, Eq. (35): Jameson-type sensor, distinct from Ducros' (arXiv v4).
