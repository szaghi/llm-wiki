---
type: Method
title: "Spectral eddy viscosity"
description: "Kraichnan's spectral eddy viscosity expresses the energy transfer across a cutoff as a wavenumber-dependent viscosity with a low-wavenumber plateau and a cusp near the cutoff; the sources use it to diagnose explicit and implicit LES, to build a modal plateau–cusp model for DG, and to compute it from the LES field itself."
status: established
aliases: [Kraichnan spectral eddy viscosity, Chollet–Lesieur model, plateau–cusp eddy viscosity, EDQNM eddy viscosity]
tags: [les, sgs-model, eddy-viscosity, implicit-les, dg]
timestamp: 2026-10-27T15:52:00Z
---

# Spectral eddy viscosity

The **spectral eddy viscosity** $\nu_t(k\mid k_c)$ is the viscosity that,
acting on the resolved spectrum at wavenumber $k<k_c$, removes the energy
that nonlinear triads transfer to the scales beyond the cutoff $k_c$. On
this page $k$ is the wavenumber magnitude, as the registry prescribes for
spectral pages. [Vicente Cruz & Lamballais (2023)](/sources/vicentecruz-2023.md)
(§2.2) cite Kraichnan's definition from the resolved (supergrid) Lin
equation. Let
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
$k\to k_c$ (Kraichnan, cited by [Flad & Gassner (2017)](/sources/flad-2017.md),
§3.1, and by Vicente Cruz & Lamballais (2023), §6.4). Vicente Cruz &
Lamballais also cite Lesieur's interpretation, which assigns the plateau to
non-local triads and the cusp to local triads. The **Chollet–Lesieur model** (from
EDQNM; Flad & Gassner 2017, App. C, Eq. C.1–C.2; Vicente Cruz & Lamballais
2023, Eq. 55) fits both:

$$\nu_t(k\mid k_c)=0.267\Big[1+34.5\,e^{-3.03\,k_c/k}\Big]\sqrt{\frac{E(k_c)}{k_c}},$$

where 0.267 is the plateau value for an infinite Kolmogorov spectrum and the
exponential is an empirical fit of the cusp. Vicente Cruz & Lamballais
(§6.4) cite Métais & Lesieur, who made the plateau depend on the spectral
slope (spectral-dynamic model).
[Domaradzki (2024)](/sources/domaradzki-2024.md) (Eq. 2.25) recalls the
same Chollet fit (TFM/EDQNM, infinite $k^{-5/3}$ range) with the Kolmogorov
constant $C_K$ kept explicit,

$$\nu_t(k\mid k_c)=\Big(\frac{E(k_c)}{k_c}\Big)^{1/2}C_K^{-3/2}\Big(0.441+15.2\,e^{-3.03\,k_c/k}\Big),$$

with $C_K$ "taken usually as 1.4"; with that value the two printed forms
coincide ($0.441\cdot1.4^{-3/2}=0.266$, $15.2/0.441=34.5$, *compiler check,
not in the sources*). Domaradzki places the plateau at $k\lesssim0.4k_c$ (§1).

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

## Eddy viscosity derived from the LES field

Domaradzki (2024, §2.2) recalls the author's spectral "autonomous" LES, in
which $\nu_t(k\mid k_c)$ is not modelled but computed at every step from
the LES field: the subgrid transfer across a sharp test cutoff $k_c/2$
gives, by Kraichnan's definition, a resolved eddy viscosity that is
rescaled to $k_c$ in the similarity variable $k/k_c$, its plateau taken
from the limit $k\to0$, and its total level set by the ultraviolet-flux
relation: the transfer across $k_c$ is the resolved transfer across $ak_c$
divided by $1-a^{4/3}$, a factor 1.66 for $a=1/2$ (Eqs. 2.26–2.27). The
physical-space version is the
[autonomous eddy-viscosity model](/methods/autonomous-eddy-viscosity-model.md).
Domaradzki compares three spectral viscosities (§3.3, Fig. 10): the
Chollet–Lesieur fit, an LES-derived cusp with a plateau at $p_{\mathrm{pl}}=0.37$ of the
cusp value at $k_c$ ($p_{\mathrm{pl}}$ page-local), and a $k$-independent viscosity
matched to the total transfer. The plateau–cusp LES-derived viscosity
agrees best with the inertial range up to $k_c$; the physical-space model
with constant $C_{\mathrm A}=0.8$ (registry §11, the non-dimensional
constant of its constant variant) practically overlaps the $k$-independent one.
Domaradzki (§3.3) also cites
Thiry, Winckelmans & Duponcheel (2019), who found the spectral viscosity
of the dynamic Smagorinsky model "essentially uniform over all
wavenumbers", and Siegel & Domaradzki (1994) found Smagorinsky spectra
approximately uniform in $k$ (§3.3), in line with the nearly constant
a posteriori Smagorinsky viscosity of Vicente Cruz & Lamballais (§6.3,
Fig. 11) above.

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
- [Domaradzki (2024)](/sources/domaradzki-2024.md) — §1; §2.2, Eqs. (2.24)–(2.27); §3.3, Fig. 10.
