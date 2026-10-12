---
type: Method
title: "Primitive-variable recovery in relativistic MHD"
description: "The pointwise inversion of the Valencia conserved variables to density, velocity and internal energy in (general-)relativistic MHD: the five schemes (three Newton–Raphson, two one-dimensional) compared by Siegel et al. on tabulated equations of state, and Kastaun et al.'s one-dimensional master function with proved root existence and uniqueness, error bounds, and built-in projection of invalid states."
status: established
aliases: [conservative-to-primitive inversion, con2prim, c2p, primitive recovery, recovery scheme, RePrimAnd, Newman–Hamlin inversion]
tags: [mhd, relativity, primitive-recovery, equation-of-state, time-integration, verification]
timestamp: 2026-10-12T00:00:00Z
---

# Primitive-variable recovery in relativistic MHD

Relativistic (M)HD codes evolve the Valencia conserved variables $D$,
$S_i$, $\tau$ (plus $\mathbf B$ and, with composition, the electron
fraction $Y_{\mathrm e}$ times $D$), but fluxes and sources need the
primitives $\rho$, $\mathbf v$, $e$ (or $T$). The map from primitives to
conserved variables is explicit; its inverse has no closed form and is
solved numerically in every cell at every evaluation of the fluxes
([Siegel et al. (2018)](/sources/siegel-2018.md), §§1–2, eqs. 8–21;
[Kastaun et al. (2021)](/sources/kastaun-2021.md), §I, §II C). Recovery
leaves the conserved variables untouched and imposes no time-step
constraint. It needs $\mathbf B$ already updated, which constrained
transport or a vector-potential scheme provide
([Kastaun et al. (2021)](/sources/kastaun-2021.md), §II C). Below,
$h_{\mathrm{rel}} = 1 + e + p/\rho$ is the relativistic specific enthalpy.

The problem is in principle five-dimensional ($\rho$, $\mathbf v$, $e$;
$\mathbf B$ and $Y_{\mathrm e}$ are trivial). Five-dimensional schemes were
"later shown to be slow and inaccurate", and reductions to one or two
scalar unknowns are preferred ([Siegel et al. (2018)](/sources/siegel-2018.md),
§3, citing Noble et al. 2006). Siegel et al. state that with a
finite-volume code the recovery schemes "are second-order accurate" and
that higher-order finite-volume schemes add complexity (§1; asserted).

## Schemes compared by Siegel et al. (2018)

[Siegel et al. (2018)](/sources/siegel-2018.md) compare five schemes for
ideal GRMHD with a three-parameter equation of state in
$(\rho, T, Y_{\mathrm e})$ (§3):

| scheme | unknowns | EOS inversion per iteration | solver |
|---|---|---|---|
| 2D NR Noble (Noble et al. 2006, extended) | $\rho h_{\mathrm{rel}}W^2$, $\vert\mathbf v\vert^2$ | $h_{\mathrm{rel}}\to T$ | Newton–Raphson |
| 2D NR | $W$, $T$ | none | Newton–Raphson |
| 3D NR (after Cerdá-Durán et al. 2008) | $W$, $\rho h_{\mathrm{rel}}W^2$, $T$ | none | Newton–Raphson |
| 1D Brent (Neilsen et al. 2014; Palenzuela et al. 2015) | $h_{\mathrm{rel}}W$, bracketed | $e\to T$ | Brent |
| 1D Newman (Newman & Hamlin 2014) | $p$ | enthalpy density $\to T$ | fixed point with a closed-form cubic, Aitken acceleration |

(§§3.1–3.4, eqs. 22–60). The 1D Brent bracket "guarantees the existence
of a root and convergence" (§4.2; asserted from the bracket property).
Several printed Newman formulas (eqs. 48, 53, 56, 58) look typo-affected
and are recorded on the [Source page](/sources/siegel-2018.md).

**Test set-up** (§4.1): forward–inverse tests only (primitives →
conserved → recovered), with an ideal gas ($\gamma = 4/3$), the partly
tabulated Helmholtz EOS and the fully tabulated LS220 EOS; initial guesses
perturbed by 5%; convergence tolerance $5\times10^{-9}$, success if the
mean relative error is below $5\times10^{-8}$. No evolution test and no
wall-clock timing.

**Cost** (§4.2, §5, Tables 1–2; measured). The schemes that need an EOS
inversion per iteration (1D Brent, 2D NR Noble, 1D Newman) need one to
two orders of magnitude more EOS calls on tabulated EOSs, because each
inversion "typically requires tens of steps ... and a few EOS calls per
step". In the density–temperature plane with LS220 the mean EOS calls are
13.0 (2D NR) and 11.3 (3D NR) against 836, 758 and 331; with the ideal gas
all schemes need under 10. The claimed speed-up of 3D NR, "at least a few
to 10, potentially up to a factor of 100", is inferred from call counts,
and the statement that recovery can take "up to ∼40%" of a simulation is
asserted without measurement.

**Accuracy** (Table 1): 3D NR is most accurate, mean relative error
$1.3\times10^{-13}$ (LS220) and $1.7\times10^{-14}$ (Helmholtz).

**Robustness** (§4.2, §5, Fig. 3, Table 2).
* The Newton–Raphson schemes need good initial guesses, hence depend on
  the previous step, and use thermodynamic derivatives, which for tables
  are numerical, noisy and "may be thermodynamically inconsistent".
  The 1D schemes need neither explicitly, but the inner inversion brings
  both back; only 1D Newman is "entirely independent of the previous time
  step".
* Enthalpy inversions (Newman, Noble) fail at very high density and low
  temperature with LS220, "less than 1.5% of the total points", because
  the first step leaves the table.
* In the Lorentz-factor–magnetization plane, which extends to
  deliberately extreme magnetizations, all schemes fail at strong field
  or high $W$; recovered fractions are 52.6–79.1%, highest for 1D Newman
  with every EOS. 2D and 3D NR fail beyond $W\approx10$ with the ideal
  gas; 3D NR reaches $W\simeq100$ (LS220) and $10^2$–$10^3$ (Helmholtz).

**Recommendation** (abstract, §5; not tested as a combined scheme): for an
analytic EOS, 1D Brent or 1D Newman, Newman preferred for accuracy; for a
three-parameter EOS, 3D NR first, falling back to 1D Brent or 1D Newman
where it fails. The open-source testbed "GRMHD con2prim" accompanies the
paper (§5).

## The master function of Kastaun et al. (2021)

[Kastaun et al. (2021)](/sources/kastaun-2021.md) reduce recovery for an
arbitrary EOS $p(\rho, e)$ to one root of
$$f_{\mathrm m}(\mu_{\mathrm r}) = \mu_{\mathrm r} - \hat\mu_{\mathrm r}(\mu_{\mathrm r}),\qquad \mu_{\mathrm r} \equiv \frac{1}{Wh_{\mathrm{rel}}},$$
where $\hat\mu_{\mathrm r}$ is recomputed from the velocity, density and
specific internal energy that a trial $\mu_{\mathrm r}$ implies, with
density and energy clamped to the EOS validity box (§II D–E,
eqs. 26, 40–48). The conserved variables enter only through $D$-rescaled
combinations, and the relevant field measure is $|\mathbf B|/\sqrt D$, of
order one already at very large magnetization (§II C). The form was found
"by trial and error": the simpler $\hat\mu_{\mathrm r} = 1/(\hat W\hat h_{\mathrm{rel}})$
kinks badly under clamping (§II E). In the Newtonian limit $f_{\mathrm m}$ is nearly
linear (§V A).

**Proved** (§II F–G, App. A):
* **Existence.** An EOS-free auxiliary function gives an explicit bracket
  $(0, \mu_+]$ in which $f_{\mathrm m}$ changes sign, so a root exists **for any
  conserved input, valid or not**; the proof uses no EOS property except a
  global lower bound of $h_{\mathrm{rel}}$.
* **Uniqueness.** At a root
  $$\frac{df_{\mathrm m}}{d\mu_{\mathrm r}} \ge 1 - \hat v^2 > 0$$
  whenever the sound speed is below 1, at any velocity and field
  (eq. 65); a further mild condition (eq. 66) applies when $e$ hits the
  upper limit of the EOS. Uniqueness on the full bracket is **not**
  proved when the density leaves its valid range; a monotone sub-bracket
  is used there instead.
* **Error bounds** (derived to linear order, §II H, eqs. 69–74): with the
  root tolerance $\Delta_\mu = \hat W^2\delta\mu_{\mathrm r}/\mu_{\mathrm r}$,
  the relative errors of $W$, $\rho$ and $h_{\mathrm{rel}}$ are at most
  $\hat v^2\Delta_\mu$, of the momentum at most $\Delta_\mu$, and the
  required tolerance tightens with $W$ but not with the field. $D$ is
  reproduced exactly. Round-off is excluded.

**Invalid states** (§III A). The recovery projects onto the valid region
and recomputes the conserved variables: below the zero-temperature energy
only $\tau$ changes, $D$ and $S_i$ do not; above the upper energy limit
all may change, meant only at fluid–vacuum boundaries or inside horizons.

**Implementation and measurements** (§IV). The C++ library RePrimAnd uses
the bracketing, derivative-free TOMS748 root finder with a bounded number
of steps and no initial guess.
* For $W|\mathbf v|$ up to 1000, $|\mathbf B|/\sqrt D$ up to 5 and thermal
  specific energy $10^{-4}$–50, with an ideal gas ($\gamma = 2$) and a
  hybrid MS1 EOS at $\Delta_\mu = 10^{-8}$, it never failed for valid input
  and needed at most **23 EOS calls**. At field measure $10^4$ and
  $W = 10^3$ it needed about 40 steps, still without failure (Figs. 4–5).
* Below $\Delta_\mu\approx10^{-7}$ the bounds are exceeded at high $W$ or
  very small $e$ and $|\mathbf v|$, attributed to round-off; with that
  included, the measured accuracy lies within the predicted bounds
  (Fig. 3). A fully tabulated three-parameter nuclear EOS was not tested
  (§IV D).

**Error amplification** (§V; measured by finite differences). In
magnetically dominated, low-density regions, evolution errors in $\tau$
and $\mathbf B$ are amplified in $e$ roughly by the ratio of magnetic (or
kinetic) to internal energy; at $10^{15}$ G a relative error $10^{-4}$
dominates $e$ near $10^8$ g cm$^{-3}$. The authors accept this as "a
fundamental consequence of evolving the conserved variables" and propose
no internal-energy or entropy fallback (compare the
[dual-energy formalism](/methods/dual-energy-formalism.md)). The
zero-temperature floor biases the energy upward and causes **spurious
heating**, without momentum drift since only $\tau$ is changed (§V D).

**Classification** (§IV D, Table I):

| scheme | unknown | EOS form | EOS derivatives | steps bounded | guess needed |
|---|---|---|---|---|---|
| Kastaun et al. | $\mu_{\mathrm r}$ | $p(\rho, e)$ | no | yes | no |
| Noble et al. | $D/\mu_{\mathrm r}$, $\vert\mathbf v\vert^2$ | $p(\rho, h_{\mathrm{rel}})$ | yes | no | yes |
| Siegel et al. (2D NR) | $D/\mu_{\mathrm r}$, $T$ | $p(\rho, T)$ | yes | no | yes |
| Cerdá-Durán et al. | $W$, $D/\mu_{\mathrm r}$, $T$ | $e(\rho, T)$ | yes | no | yes |
| Neilsen et al. | $D/\mu_{\mathrm r}$ | $p(\rho, e)$ | no | yes | no |
| Newman & Hamlin | $p$ | $p(\rho, h_{\mathrm{rel}})$ | no | yes | no |

Note $D/\mu_{\mathrm r} = \rho h_{\mathrm{rel}}W^2$. Siegel et al.'s unknown
for 1D Brent (Neilsen) in the table above, $h_{\mathrm{rel}}W = 1/\mu_{\mathrm r}$, and
Kastaun et al.'s $D/\mu_{\mathrm r}$ differ only by the known factor $D$. Reading Siegel et al.'s
figures, Kastaun et al. state that every earlier scheme fails somewhere for
$W = 10$–$1000$, also with the ideal gas, and that only Newman's needs
fewer than about 10 steps consistently; that the $5\times10^{-8}$ success
criterion is unattainable by any scheme at $W\gtrsim2\times10^3$ (small
field) or at very low magnetic-to-gas pressure ratios (small velocity),
because of cancellation in $e$; and that RePrimAnd meets it in their
standard domain except for the ideal gas at $e\lesssim0.005(W/10^3)^2$
(§IV D; comparison with published figures, not a rerun).

## In codes

[Athena++](/software/athena-plus-plus.md) inverts with the Newman & Hamlin
(2014) one-dimensional root-find
([Stone et al. (2020)](/sources/stone-2020.md), §4), the scheme that recovers the
largest fraction of points in Siegel et al.'s Lorentz-factor–magnetization
sweep and that they recommend for analytic equations of state; in their
density–temperature plane with LS220 the enthalpy inversions (Newman,
Noble) are less robust than 1D Brent, failing on up to 1.5 % of points.
Neither recovery paper tests its scheme inside an evolution code; Kastaun
et al. defer this to future work (§IV C).

## Contradictions

* **Is the extra temperature inversion an inherent cost?** *Open.*
  [Siegel et al. (2018)](/sources/siegel-2018.md), §4.2 and §5, attribute
  the 1–2 orders of magnitude more EOS calls of the energy- and
  enthalpy-based schemes to the inversion for $T$ at every iteration
  ("roughly 10–100 EOS calls by itself") and favour schemes with $T$ as
  an unknown for tabulated EOSs. [Kastaun et al. (2021)](/sources/kastaun-2021.md),
  §IV D, call the extra inversion a shortcoming of EOS implementations:
  their own inversion uses discrete bisection plus inverse interpolation in
  fewer than 10 steps. They concede that Siegel et al.'s schemes "might
  indeed be faster" with a temperature-based table. Neither paper times
  the alternatives on the same tabulated EOS.

# Citations

1. [Siegel et al. (2018)](/sources/siegel-2018.md), §§1–5, eqs. 8–61,
   Tables 1–2, Figs. 1–3 (arXiv v2).
2. [Kastaun et al. (2021)](/sources/kastaun-2021.md), §§I–V, eqs. 2–82,
   Table I, App. A (arXiv v2).
3. [Stone et al. (2020)](/sources/stone-2020.md), §4.
