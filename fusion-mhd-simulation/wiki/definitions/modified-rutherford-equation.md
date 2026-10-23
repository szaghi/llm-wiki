---
type: Definition
title: "Modified Rutherford equation"
description: "The evolution equation for the width of a thin, single-helicity magnetic island in the nonlinear (Rutherford) regime, in which the island grows on the resistive time at a rate set by the tearing index plus bootstrap, curvature (D_R) and other corrections; used in the sources as a fit to simulated island growth, as an NTM growth check and through its time-rescaling invariance."
status: established
aliases: [MRE, Rutherford equation, Rutherford regime, island width equation]
tags: [tearing, extended-mhd, bootstrap-current]
timestamp: 2026-10-16T18:35:00Z
---

# Modified Rutherford equation

Once a [tearing mode](/definitions/tearing-mode.md) island is wider than the
linear resistive layer, the exponential growth of linear theory gives way to
the **Rutherford regime**, in which the island width $w$ grows algebraically on
the resistive time. The classical Rutherford result is
$dw/dt\propto(\eta/\mu_0)\,\Delta'$; the **modified Rutherford equation**
(MRE) adds to $\Delta'$ the terms that matter in toroidal, finite-$\beta$
plasmas: the bootstrap-current drive of
[neoclassical tearing modes](/definitions/neoclassical-tearing-mode.md), the
Glasser–Greene–Johnson curvature term, polarization and saturation terms.
Below, $w$ is the full island width, $r_s$ the radius of the resonant
surface, $\tau_R=\mu_0r_s^2/\eta$ the local resistive time, and $D_R$ the
resistive-interchange parameter (registry §10; $\tau_R$ here built on $r_s$).

## Forms printed in the sources

**Lütjens–Luciani–Garbet form.** With a saturation width $w_{\rm sat}$ and a
small-island width $w_d$,

$$\frac{dw}{dt}=\frac{1.22}{\tau_R}\Big[\Delta'\Big(1-\frac{w}{w_{\rm sat}}\Big)+\frac{6.35\,D_R}{\sqrt{w^2+0.65\,w_d^2}}\Big]$$

([Zeng et al. (2023)](/sources/zeng-2023.md), Eq. 7, after Lütjens et al.
2001). The $D_R$ term carries the curvature (favourable-average-curvature)
effect of finite pressure. $D_R$ is normally negative and stabilizing; it
becomes positive when the local pressure gradient reverses (see
[radiation-triggered tearing](/results/radiation-triggered-tearing.md)).

**An ad hoc fit.** To match their NIMROD island growth, Zeng et al. write

$$\tau_R\frac{dw}{dt}=\lambda_{\rm f}\Big(\Delta'_0+\alpha_{\rm f,2}D_R-\alpha_{{\rm f},1}\frac{j_{{\rm PS},2/1}}{j_{{\rm PS},0}}\Big),$$

with $\Delta'_0$ the tearing index measured in the simulation, $j_{{\rm PS},2/1}$
the $2/1$ Pfirsch–Schlüter current in the layer and $j_{{\rm PS},0}$ its
equilibrium value, and three fitted constants $\lambda_{\rm f}=35$,
$\alpha_{\rm f,1}=0.5$, $\alpha_{\rm f,2}=10$ (Eq. 8, Fig. 4a; page-local
symbols). The authors call the form "crude". As printed, the left side has
units of length and the right side mixes an inverse length with
dimensionless terms, so the fitted constants carry hidden dimensions
(recorded on the [Source page](/sources/zeng-2023.md)).

**Island width from the helical flux.** For a thin single-helicity island
NIMROD diagnostics use $w=\frac{4}{2\pi}\sqrt{\frac{q}{q'}\frac{|\Psi_{m/n}|}{m}}$,
with $\Psi_{m/n}$ the resonant helical flux and $q'$ the derivative with
respect to the poloidal flux; for the DIII-D $2/1$ case this is
$w\,[\mathrm{cm}]=1.54\sqrt{|\Psi_{2/1}|\,[\mathrm{mWb}]}$
([Howell et al. (2022)](/sources/howell-2022.md), Eqs. 14–16). Because the
helical flux scales as $w^2$, a constant $dw/dt$ (classical Rutherford) gives
quadratic growth of the flux and an NTM gives linear growth (§III B).

None of the ingested sources prints the bootstrap term of the MRE (none of
the chunk-3 sources uses the MRE); Howell et
al. use an MRE evaluated in a companion paper (their ref. [30], in
preparation).

## Uses in the sources

* **Onset fit.** The Lütjens form with $\Delta'=120$, $w_{\rm sat}=0.1$ m
  and $w_d=0.02$ m reproduces the trend of the impurity-triggered $2/1$ onset
  for $t<0.5$ ms but fails afterwards, when $D_R$ relaxes to about zero while
  the island keeps growing; the ad hoc form fits the whole evolution
  ([Zeng et al. (2023)](/sources/zeng-2023.md), §3, Figs. 3b, 4a). The
  $\Delta'=120$ (units not printed) used in the fit is positive although the
  equilibrium is called tearing-stable.
* **NTM growth check.** The robust-phase growth of the simulated $2/1$ NTM in
  DIII-D, about 3.4 Wb/s, agrees with 3.3 Wb/s from the MRE with the
  simulated parameters, which the authors read as "standard NTM growth"; the
  same analysis finds the classical $\Delta'$ negligible in that plasma
  ([Howell et al. (2022)](/sources/howell-2022.md), §III B, §V).
* **Rescaling invariance.** In the Rutherford regime $dw/dt\propto\eta$, so the
  evolution is invariant under $t\to\alpha t$, $\eta\to\eta/\alpha$. JOREK
  runs of a $4/1$ [double tearing mode](/definitions/double-tearing-mode.md)
  at $\eta=10^{-6}$ and $3\times10^{-7}$ (JOREK units) collapse onto each
  other for $n=1,2$ after rescaling time by 3.3, the resistivity ratio
  ([Nardon et al. (2023b)](/sources/nardon-2023-b.md), §IV.A, Fig. 7). Inside
  a Rutherford island the current density divided by $B$ tends to be constant
  on helical flux surfaces (§IV.A, Fig. 10).
* **Linear versus Rutherford competition.** A secondary mode still in its
  linear regime ($\gamma\propto\eta^{3/5}$) grows, relative to a primary in
  the Rutherford regime ($\propto\eta$), as $\eta^{-2/5}$: secondaries win at
  low resistivity. This is the heuristic Nardon et al. use to explain the
  resistivity window of violent double-tearing relaxation (§IV.A). A critical
  $\Delta'$ for visco-resistive modes scaling as $\eta^{1/6}\nu^{1/6}$ (Grasso
  et al. 2008, cited there) differs by only about 20% between their cases,
  and a tenfold viscosity reduction has almost no effect.

## Contradictions

None open. The sources use the MRE as a fit or a check, not as competing
derivations.

# Citations

- [Zeng et al. (2023)](/sources/zeng-2023.md) — §3, Eqs. 7–8, Figs. 3b, 4a.
- [Howell et al. (2022)](/sources/howell-2022.md) — §III B, §V, Eqs. 14–16, Fig. 5A.
- [Nardon et al. (2023b)](/sources/nardon-2023-b.md) — §IV.A, Figs. 7, 10.
