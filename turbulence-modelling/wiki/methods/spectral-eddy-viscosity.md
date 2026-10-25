---
type: Method
title: "Spectral eddy viscosity"
description: "Kraichnan's spectral eddy viscosity expresses the energy transfer across a cutoff as a wavenumber-dependent viscosity with a low-wavenumber plateau and a cusp near the cutoff; the sources use it to diagnose explicit and implicit LES and to build a modal plateau–cusp model for DG."
status: established
aliases: [Kraichnan spectral eddy viscosity, Chollet–Lesieur model, plateau–cusp eddy viscosity, EDQNM eddy viscosity]
tags: [les, sgs-model, eddy-viscosity, implicit-les, dg]
timestamp: 2026-10-25T13:42:00Z
---

# Spectral eddy viscosity

The **spectral eddy viscosity** $\nu_t(k\mid k_c)$ is the viscosity that,
acting on the resolved spectrum at wavenumber $k<k_c$, removes the energy
that nonlinear triads transfer to the scales beyond the cutoff $k_c$. On
this page $k$ is the wavenumber magnitude, as the registry prescribes for
spectral pages. As recalled by
[Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) (§2.2),
Kraichnan defined it from the resolved (supergrid) Lin equation. Let
$\bar E(k)$ be the resolved spectrum, and $T_<(k)$, $T_>(k)$ the transfer
into $k$ from resolved and from subgrid interactions (page-local symbols).
With exact differentiation the resolved dissipation spectrum is
$2\nu k^2\bar E(k)$, and

$$\partial_t\bar E=T_<+T_>-2\nu k^2\bar E,\qquad
\nu_t(k\mid k_c)=-\frac{T_>(k)}{2k^2\bar E(k)},$$

so that $\partial_t\bar E=T_<-2(\nu+\nu_t)k^2\bar E$ (Vicente Cruz &
Lamballais 2023, Eqs. 16–22, with $\bar\varepsilon=2\nu k^2\bar E$
substituted in their Eq. 21). A positive $\nu_t$ means net forward transfer
at that wavenumber. Being a shell average, $\nu_t(k\mid k_c)$ measures only
the net transfer across the cutoff, not its local sign in space *(compiler
check, not in the sources)*; see [energy backscatter](/definitions/energy-backscatter.md).

## Plateau and cusp

For a cutoff inside an infinite inertial range the spectral eddy viscosity
is a constant **plateau** at low $k$ that rises to a **cusp** as
$k\to k_c$ (Kraichnan, as recalled by [Flad & Gassner 2017](/sources/flad-2017.md),
§3.1, and by Vicente Cruz & Lamballais 2023, §6.4). Lesieur's interpretation,
recalled by Vicente Cruz & Lamballais, assigns the plateau to non-local
triads and the cusp to local triads. The **Chollet–Lesieur model** (from
EDQNM; Flad & Gassner 2017, App. C, Eq. C.1–C.2; Vicente Cruz & Lamballais
2023, Eq. 55) fits both:

$$\nu_t(k\mid k_c)=0.267\Big[1+34.5\,e^{-3.03\,k_c/k}\Big]\sqrt{\frac{E(k_c)}{k_c}},$$

where 0.267 is the plateau value for an infinite Kolmogorov spectrum and the
exponential is an empirical fit of the cusp. Métais & Lesieur made the
plateau depend on the spectral slope (spectral-dynamic model), as recalled
by Vicente Cruz & Lamballais (§6.4).

## A priori estimates against the model

Vicente Cruz & Lamballais (2023, §6.4, Figs. 16–19) estimate
$\nu_t(k\mid k_c)$ a priori from filtered DNS of the
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) at $Re=40\,000$
($5400^3$ DNS, LES cutoffs $k_c=108$, 270, 540):

- the plateau is nonzero, about 12, 2 and 0.2 times $\nu$ at the three
  cutoffs ($t=10$), and is insensitive to the filter shape;
- the subgrid dissipation carried by $k<k_c/4$ reaches 24%, 16% and 6% of
  the total dissipation;
- with a sharp cutoff the a priori curve matches Eq. (55) in plateau and
  cutoff value at $t=10$; with the super-Gaussian filter, the plateau agrees
  if the comparison uses an equivalent sharp cutoff $k_c=68$ (same captured
  energy as the super-Gaussian at 108); at $t=15$ the a priori plateau is
  more than twice lower than Eq. (55), attributed to the drop of
  $Re_\lambda$ from about 493 to 389;
- the cusp of a non-idempotent filter is more than an order of magnitude
  higher than the sharp-cutoff cusp, so "there is no reason to design SGS
  modelling to match quantitatively this specific cusp when a different
  filtering is expected".

The a posteriori spectral viscosity of an LES model is measured from the
model's own dissipation spectrum (Eqs. 27–29). For constant-coefficient
[Smagorinsky](/methods/smagorinsky-model.md) at numerical convergence it is
of the right order at low $k$ but nearly constant, and vanishes near $k_c$
where the a priori curve rises (§6.3, Fig. 11). For the implicit
[spectral vanishing viscosity](/methods/spectral-vanishing-viscosity.md) it
reproduces the cusp but vanishes at low $k$, missing the plateau (§6.4).
From this missing plateau the authors conclude that the plateau "cannot
be ignored, making somewhat inconsistent the concept of
[implicit LES](/definitions/implicit-les.md) except when the mesh is close
to DNS" (§6.4).

## Plateau–cusp model in modal DG space

Flad & Gassner (2017, §3.1) explain the failure of DG implicit LES at coarse
resolution by the shape of interface dissipation: concentrated at the
highest wavenumbers, without the low-wavenumber plateau. Their third "cusp"
strategy (§5, App. C, Eqs. C.3–C.5) transfers the cusp to modal polynomial
space,

$$\nu_t^+(N+1\mid N_c+1)=9.21\,e^{-3.03\,(N_c+1)/(N+1)},$$

with $N_c$ a modal cutoff (page-local), and uses it as the weighting of a
polynomial high-pass filter applied to the lifted gradients. The cusp
stress $-2C_{\mathrm{cusp}}\Delta^2\lvert S\rvert S^d_{ij}$ of the
filtered gradients, with $C_{\mathrm{cusp}}=0.33^2$, is added to a
Smagorinsky stress with $C_s=0.13$, on a dissipation-free kinetic-energy-preserving
split-form DG baseline. On decaying HIT at $48^3$ degrees of freedom it
gives the best fit to the DNS spectrum of the three strategies tested, but
leaves the pressure–dilatation oscillations unchanged (§5, §5.1, Figs. 8,
10).

## Qualifications

- $9.21=0.267\times34.5$ *(compiler check, not in the sources)*: Eq. (C.3)
  of Flad & Gassner keeps only the cusp part of Eq. (C.2) and drops the
  plateau term although the model is named "plateau–cusp"; Eqs. (C.2)–(C.3)
  also print unbalanced parentheses.
- Vicente Cruz & Lamballais (2023) print the a priori estimator (Eq. 23)
  without the leading minus sign that follows from their Eqs. (18), (20)
  and (21) *(compiler check, not in the sources)*; as printed it would give
  a negative viscosity for forward transfer. The plateau values they report
  in the text (12, 2 and 0.2 times $\nu$) are positive, consistent with the
  corrected sign.

# Citations

- [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md) — §2.2, Eqs. (16)–(23), (27)–(29); §6.3, Fig. 11; §6.4, Eq. (55), Figs. 16–19.
- [Flad & Gassner (2017)](/sources/flad-2017.md) — §3.1; §5, Fig. 8; §5.1, Fig. 10; App. C, Eqs. (C.1)–(C.5).
