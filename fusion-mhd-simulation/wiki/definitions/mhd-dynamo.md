---
type: Definition
title: "MHD dynamo effect"
description: "The axisymmetric electromotive force produced by correlated non-axisymmetric velocity and field fluctuations, which redistributes the mean current; in nonlinear tokamak simulations a slow negative dynamo of a few mV/m clamps q0 in flux pumping and a fluctuation-induced emf builds counter-current sheets in peeling-ballooning ELMs."
status: established
aliases: [dynamo, fluctuation-induced emf, mean-field dynamo, negative dynamo, fast dynamo, slow dynamo, parallel dynamo emf]
tags: [full-mhd, kink, elm, tokamak]
timestamp: 2026-10-16T23:45:00Z
---

# MHD dynamo effect

In a toroidal plasma with non-axisymmetric modes, the MHD dynamo is the
electromotive force that the correlated fluctuations of velocity and
magnetic field exert on the axisymmetric (mean) field, "the
fluctuation-induced emf along the mean magnetic field" (Ji & Prager 2001,
as cited by [Zhang et al. (2025)](/sources/zhang-2025.md), §1). It moves
current across flux surfaces without a crash, and it is the mechanism of
[magnetic flux pumping](/definitions/magnetic-flux-pumping.md). Hall and
diamagnetic dynamos exist in extended models; the sources here compute only
the MHD ($\mathbf v\times\mathbf B$) part (Zhang et al. 2025, §1).

## Definition in the sources

Split every field into its toroidal average, $f^{(0)}$ (the $n=0$
harmonic), and the non-axisymmetric remainder $\tilde f=f-f^{(0)}$
(registry §11). The toroidal average of
$\mathbf v\times\mathbf B$ then contains a mean-field part and a
fluctuation part,

$$\big(\mathbf v\times\mathbf B\big)^{(0)}=\mathbf v^{(0)}\times\mathbf B^{(0)}+\big(\tilde{\mathbf v}\times\tilde{\mathbf B}\big)^{(0)},$$

and the second term is the fluctuation-induced emf.

* **Toroidal balance.** With $\psi=RA_\phi$ (per radian), Faraday's law in
  the Weyl gauge and a resistive term acting only toroidally, the
  axisymmetric flux evolves as
  $$\partial_t\psi^{(0)}=R\Big[\big(\mathbf v^{(0)}\times\mathbf B^{(0)}\big)_\phi+\big(\tilde{\mathbf v}\times\tilde{\mathbf B}\big)^{(0)}_\phi-\eta^{(0)}\big(j_\phi^{(0)}-J_{x,\phi}\big)-\big(\tilde\eta\,\tilde j_\phi\big)^{(0)}\Big],$$
  with $\mathbf J_x$ the non-inductive source current
  ([Zhang et al. (2025)](/sources/zhang-2025.md), Eqs. 5–6, written in
  JOREK units there). The first two terms together are the "net dynamo"
  field $(\mathbf v\times\mathbf B)^{(0)}_\phi$ of that paper (§4.1).
* **Parallel dynamo field.** Projecting the mean induction equation on the
  mean field gives a parallel emf supplied "solely" by the $n\ge1$
  harmonics,
  $$E_{\mathrm{dyn},\parallel}=\Big\langle\frac{\mathbf B^{(0)}\cdot\big(\tilde{\mathbf v}\times\tilde{\mathbf B}\big)^{(0)}}{B_{\phi,\mathrm{eq}}}\Big\rangle,$$
  with $\langle\cdot\rangle$ the flux-surface average and $B_{\phi,\mathrm{eq}}=F/R$
  the equilibrium toroidal field, used instead of $|\mathbf B^{(0)}|$
  "because it has lower numerical noise" (Zhang et al. 2025, Eqs. 9–10,
  §4.2). $E_{\mathrm{dyn},\parallel}$ is the registry symbol (§11).
* **Toroidal emf map.** [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md)
  (p. 4, Fig. 6d) plot the toroidal component of the toroidally averaged
  $\tilde{\mathbf v}\times\tilde{\mathbf B}$ of the fluctuations in the
  poloidal plane, the same quantity as the second term above.

**Sign classes.** A dynamo that opposes the externally driven current is
called negative; a fast dynamo acts faster than resistive diffusion and a
slow one on the resistive time (Zhang et al. 2025, §1, §3.3–3.4).

## Dynamo in flux pumping (JOREK, ASDEX Upgrade)

In the full-MHD simulation of the AUG hybrid discharge #36663 the dynamo
appears in two forms ([Zhang et al. (2025)](/sources/zhang-2025.md)):

* **Fast dynamo.** At the saturation of the $n=1$ quasi-interchange the
  parallel emf reaches about 1.5 V/m, alternates sign at 5.8 kHz together
  with a damped oscillation of $q_0$ around 1.013 and changes sign around
  $\sqrt{\psi_N}\approx0.2$ (§3.3, Fig. 7).
* **Slow negative dynamo.** In the quasi-stationary state it is three orders
  of magnitude smaller. At 505 ms $E_{\mathrm{dyn},\parallel}$ is about
  $-1.7$ mV/m near $\sqrt{\psi_N}\approx0.07$ and $+0.5$ mV/m near 0.3
  (figure reading), dominated by $n=1$ (§4.2, Fig. 15).
* **Balance.** The electric-field deficit $\eta\,\Delta j_\phi\approx-1.6$
  mV/m between the 3D and 2D runs (with $\Delta j_\phi$ the 3D minus 2D
  current) is closed by a net dynamo of $-0.3$, $-1.35$ and $-1.6$ mV/m at
  90, 205 and 505 ms plus resistivity flattening of about 0, $-0.25$ and
  $-0.3$ mV/m (§4.1, Eq. 8, Fig. 13). The two dynamo pieces are individually
  large and of opposite sign, about $-3$ mV/m from
  $(\tilde{\mathbf v}\times\tilde{\mathbf B})^{(0)}_\phi$ and $+3$ mV/m from
  $(\mathbf v^{(0)}\times\mathbf B^{(0)})_\phi$ near $\sqrt{\psi_N}\approx0.2$
  (figure reading on the Source page), so the net value is a strong
  cancellation. The mean-flow term is "non-ignorable" in 3D, contrary to the
  $\mathbf v^{(0)}\simeq0$ assumption of Krebs et al. 2017 (as cited); in 2D
  that assumption holds. The nonlinear resistive term
  $(\tilde\eta\,\tilde j_\phi)^{(0)}$ is about $10^{-3}$ mV/m.
* **Residue.** The right-hand side slightly exceeds the deficit; the
  remainder becomes a radially flat, time-constant drift of $\psi$ after
  363 ms, which leaves $q$ and $j_\phi$ unchanged (§4.1, Fig. 14).
* **Self-scaling.** The dynamo amplitude rescales itself with $\eta$ to
  balance the drive (§6.2, stated), which is why runs at enhanced
  resistivity overestimate it, at about 0.1 V/m against the mV/m level that
  matches the experimental order of magnitude (§1, §4.1; Krebs et al. 2017
  as cited). The dynamo grows with the source strength and follows the
  source shape, on-axis peaked for an on-axis source (§5, Fig. 18).

Jardin, Ferraro and Krebs (2015, as cited by Zhang et al. 2025, §1) found
earlier, in nonlinear simulations, that a negative dynamo from correlated
$n=1$ fluctuations clamps $q_0$.

## Dynamo in peeling–ballooning ELMs (NIMROD)

In NIMROD resistive-MHD runs of DIII-D peeling–ballooning ELMs, the
fluctuation-induced toroidal emf has a bi-directional poloidal
cross-section "consistent with formation of axisymmetric toroidal current
density" ([Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md),
p. 4, Fig. 6d). The resulting axisymmetric counter-current sheet opposes
the equilibrium edge current and removes the peeling drive, the relaxation
phase of the ELM (pp. 2–4; see
[edge-localized mode](/definitions/edge-localized-mode.md)). No quantitative
balance against the $n=0$ current evolution is given, and the printed
component orientations make the emf sign unusable quantitatively (recorded
on [plasmoid instability](/definitions/plasmoid-instability.md) and the
Source page).

## Contrast

Both sources find a negative dynamo: in the core it holds the current
profile flat against a peaking source, at the edge it suppresses the
peeling current. The core case is a balance over hundreds of ms with mV/m
fields; the edge case is a transient of about a ms with an emf map of about
$\pm6$–$8\times10^3$ V/m (Ebrahimi & Bhattacharjee 2023, Fig. 6d, as read on
the Source page). Neither
source compares the two (compiler's observation).

## Qualifications

* **Numerics.** The mV/m balance relies on a 2D reference run and on
  linearizing $\eta$ about it (Zhang et al. 2025, Eq. 8); the $\eta$ term acts
  only toroidally in that model, so $A_R$, $A_Z$ and $B_\phi$ evolve
  ideally (§4.1).
* **Viscosity.** The flow amplitude, and therefore the dynamo, depends on a
  viscosity the paper calls a free parameter (§6.2).

## Contradictions

None open on the dynamo itself. The flux-pumping question of whether $q_0$
is held at or above 1 is recorded on
[magnetic flux pumping](/definitions/magnetic-flux-pumping.md).

# Citations

- [Zhang et al. (2025)](/sources/zhang-2025.md) — §1, §3.3–3.4, §4.1–4.3, §5, §6.2, Eqs. 5–12, Figs. 7, 13–15, 18.
- [Ebrahimi & Bhattacharjee (2023)](/sources/ebrahimi-2023.md) — pp. 2–4, Fig. 6d.
