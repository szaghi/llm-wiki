---
type: Definition
title: "Ducros shock sensor"
description: "The Ducros sensor flags compressions by the share of dilatation in the velocity-gradient magnitude; the page gives the classical squared ratio, the modified compression-only form that switches hybrid central/TENO and central/WENO schemes, its regularization and thresholds, and its recorded failures and repairs."
status: established
aliases: [Ducros sensor, modified Ducros sensor, improved Ducros sensor, Ducros dilatation–vorticity sensor, Ducros level, dilatation-to-vorticity ratio]
tags: [central-scheme, teno, weno, finite-difference, turbulence]
timestamp: 2026-10-23T16:00:00Z
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
[De Vanna et al. (2023c)](/sources/devanna-2023-c.md)).

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
  §5.4; [adaptive TENO](/methods/adaptive-teno.md)).

**Repair by multiplication.** Sciacovelli et al. (§3, Eq. (36)) multiply the
classical ratio by the Bhagatwala–Lele dilatation switch and Jameson's
pressure sensor ($\Xi_i$, written out on
[troubled-cell indicators](/definitions/troubled-cell-indicator.md) and
[numerical dissipation](/definitions/numerical-dissipation.md)). On the
underexpanded jet the product confines the low-order dissipation to the
intercepting shocks, the Mach disk and the reflected shocks, with values below
$0.02$ elsewhere (§5.1, Fig. 8).

## Qualifications

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
