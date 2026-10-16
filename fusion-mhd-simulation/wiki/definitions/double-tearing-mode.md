---
type: Definition
title: "Double tearing mode"
description: "A tearing mode with two resonant surfaces of the same helicity in a non-monotonic q profile, whose coupled islands can relax the current profile violently; in 3D JOREK simulations of a 4/1 mode in a JET runaway-beam-like plasma the violent, helicity-conserving global relaxation with a ~30% current spike occurs only at intermediate resistivity, set by how fast secondary tearing modes grow relative to the primary."
status: established
aliases: [DTM, 4/1 double tearing mode, double tearing]
tags: [tearing, reduced-mhd, runaway-electrons, disruption, tokamak]
timestamp: 2026-10-16T12:00:00Z
---

# Double tearing mode

A double tearing mode (DTM) is a [tearing mode](/definitions/tearing-mode.md)
in a non-monotonic $q$ profile (hollow current, reversed shear) that has two
resonant surfaces of the same helicity $m/n$. The two island chains couple,
and the nonlinear dynamics can be "explosive". Two-dimensional helically
symmetric studies found explosive behaviour in parts of parameter space but
exclude stochasticity, which 3D studies show is essential
([Nardon et al. (2023b)](/sources/nardon-2023-b.md), §I).

## Kadomtsev prediction

The post-reconnection state is predicted, as for the
[sawtooth crash](/definitions/sawtooth-crash.md), by matching surfaces of
equal helical flux, here $\psi_{\rm h}=\int(1/q-n/m)\,d\psi_{t,N}$
(page-local symbol). The reconnection region is where the radius becomes a
multiple-valued function of the initial $\psi_{\rm h}$. For the case below it
extends "from almost the very centre up to the edge", because the outer $q=4$
surface lies close to the edge of a limiter plasma. In the earlier Tore Supra
DTM studies (Maget et al. 2007, 2014) the predicted region did not reach the
edge, and those simulations relaxed only partially (Nardon et al. 2023b, §I,
§II, Fig. 2). In a divertor plasma $q\to\infty$ at the edge would sharpen
$\psi_{\rm h}$ and could keep the region from the edge, although strong
shear favours island overlap (§II).

## The JET-like 4/1 case

* **Model.** JOREK pressureless [reduced MHD](/methods/reduced-mhd.md) without
  parallel flow: $\psi$ and $u$ evolved, flat density
  ($\rho=3.3\times10^{-8}$ kg m$^{-3}$), constant $\eta$ and viscosity
  ($\nu=\eta$ in JOREK units), source term $\eta(j-j_0)$, fixed boundary;
  $120\times64$ Bézier cells and $n=0$–15 (Nardon et al. 2023b, §II, Eqs.
  1–2). No runaway electrons are included, although the setup is the JET
  runaway-beam benign-termination case (Bandaru et al. 2021).
* **Equilibrium.** $R_0=2.6$ m, $a=0.67$ m, $B_\phi=3.5$ T, $I_p=0.75$ MA,
  nearly circular limiter plasma; $q_{\min}\approx3.5$ near $s=\sqrt{\psi_N}\approx0.6$
  (figure reading), $q\approx5$ at the edge and $\approx7$ near the axis, with
  two $q=4$ surfaces and $q=11/3$ and $7/2$ surfaces. The Dirichlet boundary
  suppresses the $5/1$ mode although $q_{\rm edge}\approx5$ (§II).
* **Violent relaxation at $\eta=10^{-6}$** (Spitzer at 27 eV): two $4/1$
  chains form (3.62 ms), overlap and make the field stochastic around an intact
  core (4.30 ms); a macroscopic $4/1$ flow "stirs" the plasma (4.35 ms); all
  flux surfaces are destroyed, $j_\phi/B$ flattens almost completely, and
  surfaces promptly reform (4.40–4.57 ms). The plasma current spikes by about
  30% at 4.36 ms, the internal inductance $l_i(3)$ falls to about 0.58 of its
  initial value, the $n=0$ magnetic energy drops by a few percent and the
  magnetic helicity $\int\mathbf A\cdot\mathbf B\,dV$ stays nearly constant,
  as fast-relaxation theory expects (§III, Figs. 3–4; spike and $l_i$ ratios
  read from the figure). Later spikes at 5.35 and 6.08 ms arise because the
  source term restores an unstable profile. In this model the helicity is
  dissipated only resistively,
  $\frac{d}{dt}\int\mathbf A\cdot\mathbf B\,dV\propto F_0\int\eta(j-j_0)R^{-1}\,d\phi\,dS$
  (App. A, Eq. A4; the intermediate Eq. A3 omits a Jacobian factor, see the
  Source page). The current spike connects to the disruption current spike
  on [disruption](/definitions/disruption.md).

## Resistivity window and secondary modes

The violent global relaxation occurs only for
$5\times10^{-7}\le\eta\le3\times10^{-6}$ (JOREK units; Spitzer 47–13 eV)
(Nardon et al. 2023b, §IV, Fig. 5; Hoelzl et al. 2024 present the same result
in their §3.5, Fig. 12, citing it). The explanation is the growth of
secondary tearing modes, destabilized by the steep $j_\phi$ gradient at the
outer edge of the outer $4/1$ island, relative to the primary:

* **Intermediate $\eta$.** A secondary $7/2$ mode, excited near 4 ms when the
  gradient crosses $q=7/2$, boosts stochasticity and acts as a "magnetic
  trigger" (§IV.A).
* **Low $\eta$** ($\le3\times10^{-7}$). An $11/3$ mode grows earlier and
  faster in rescaled time: it is in its linear regime ($\gamma\propto\eta^{3/5}$)
  while the $4/1$ is in its Rutherford regime ($\propto\eta$), so its relative
  growth scales as $\eta^{-2/5}$ (see
  [modified Rutherford equation](/definitions/modified-rutherford-equation.md)).
  Its early, localized stochasticity relaxes the gradient gently and removes
  the drive of the $7/2$ trigger, giving "gentle saturation" (Figs. 6–10). The
  $\eta=10^{-7}$ and $3\times10^{-7}$ runs were stopped before a possible
  later spike.
* **High $\eta$** ($\ge10^{-5}$). The $7/2$ mode never grows much, no large
  stochastic region forms, and the current spike is small (§IV.B, Figs. 13–14).

Two numerical experiments support the picture: lowering $\eta$ mid-run after
the gradient has passed $q=11/3$ still gives a large spike, and truncating to
$n=0$–2 makes the two resistivities behave alike, with no violent relaxation
in either (Figs. 11–12). Hoelzl et al. (2024, §3.5) summarize the trend as
faster secondary growth and earlier stochasticity at lower $\eta$ for the same
main-mode amplitude.

## Runaway-beam termination

The $n=1$ DTM at two $q=4$ surfaces is the mode that terminates the JET
runaway beam benignly, with losses within about 100 µs
([Hoelzl et al. (2021)](/sources/hoelzl-2021.md), §6; see
[runaway electrons](/definitions/runaway-electrons.md)). Nardon et al. (2023b,
§V) hypothesize that the different outcomes of D$_2$ and high-$Z$ injection
into runaway beams come from the background resistivity: after D$_2$
injection the colder plasma ($\eta\gtrsim10^{-5}$, about 6 eV) lets the
primary grow larger before stochasticity sets in. This is stated, not
simulated. With runaway electrons carrying the current, the finite-resistivity
correction that lowers the linear growth below $\eta^{3/5}$ at large $\eta$
is absent (Helander et al. 2007, cited in §V), which weakens one supporting
argument. In DIII-D the terminating mode is a resistive kink at $q_a\to2$
([Liu et al. (2021)](/sources/liu-2021.md); see
[tearing mode](/definitions/tearing-mode.md)).

## Contradictions

None open. The partial relaxation of the Tore Supra studies and the global
relaxation here are explained by the extent of the Kadomtsev region, not by a
disagreement between models.

# Citations

- [Nardon et al. (2023b)](/sources/nardon-2023-b.md) — §I–V, Eqs. 1–2, A1–A4, Figs. 1–14.
- [Hoelzl et al. (2024)](/sources/hoelzl-2024.md) — §3.5, Fig. 12.
- [Hoelzl et al. (2021)](/sources/hoelzl-2021.md) — §6 (JET benign termination by an n = 1 DTM).
- [Liu et al. (2021)](/sources/liu-2021.md) — DIII-D termination by the (2,1) resistive kink.
