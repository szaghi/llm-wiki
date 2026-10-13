---
type: Method
title: "Primitive-variable recovery in relativistic MHD"
description: "The pointwise inversion of the Valencia conserved variables to density, velocity and internal energy in (general-)relativistic MHD: the five schemes (three Newton–Raphson, two one-dimensional) compared by Siegel et al. on tabulated equations of state, and Kastaun et al.'s one-dimensional master function with proved root existence and uniqueness, error bounds, and built-in projection of invalid states."
status: established
aliases: [conservative-to-primitive inversion, con2prim, c2p, primitive recovery, recovery scheme, RePrimAnd, Newman–Hamlin inversion]
tags: [mhd, relativity, primitive-recovery, equation-of-state, time-integration, verification]
timestamp: 2026-10-13T00:00:00Z
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

## Later uses (batch 3)

Two GPU codes report recovery schemes inside evolution codes.

* **[GRaM-X](/software/gram-x.md)** ([Shankar et al. (2023)](/sources/shankar-2023.md),
  §II C) uses the chain Siegel et al. recommend for a three-parameter
  EOS, with a third stage added: a 3D Newton–Raphson in $W$,
  $\rho h_{\mathrm{rel}}W^2$ and $T$ first; on non-convergence the Newman &
  Hamlin one-dimensional iteration; as last resort bisection in
  temperature, "guaranteed to converge ... but much more expensive". The
  ordering is justified by "the number of EoS calls is ∼ 20 times larger in
  case of Newman's method compared to 3D-NR", citing Siegel et al. That is
  a rounded figure: the ratio of the LS220 density–temperature means above
  is 331/11.3 ≈ 29, and with the ideal gas all schemes need under 10.
  Listed failure modes: non-convergence, negative density or pressure,
  speed above $c$, and leaving the table bounds in $\rho$, $T$,
  $Y_{\mathrm e}$. The tabulated EOS (19 quantities in
  $(\rho, T, Y_{\mathrm e})$) sits in CUDA unified memory. No tolerances,
  failure statistics or recovery timings are reported.
* **[AthenaK](/software/athenak.md)** ([Stone et al. (2026)](/sources/stone-2026.md),
  §3.5–§3.6) uses the Kastaun et al. (2021) recovery for special- and
  general-relativistic hydro and MHD, "in a departure from Athena++", with
  frame transformations in GR. The evidence of robustness is visual: the
  Komissarov cylindrical explosions with field 0.1 and 1, run "robustly"
  together with a first-order flux fallback (Fig. 10), and a
  Blandford–Znajek monopole at magnetization 100 (Fig. 13). Cost
  (Table 2, Mzone-cycles/s per device): on an Intel Xeon Gold 6326
  SR-hydro (16) runs slower than SR-MHD (20), attributed to the recovery
  root finder: "Likely this algorithm requires further tuning on CPUs". On
  an NVIDIA A100 the order is reversed (378 against 178).

With these, Kastaun et al.'s scheme has been run inside an evolution code,
which the two recovery papers had left open; neither code paper reports a
recovery failure rate.

## Later uses (batch 4)

The codes of the [EHT GRMHD code comparison](/results/eht-grmhd-code-comparison.md)
document their recovery chains inside production evolution codes
([Porth et al. (2019)](/sources/porth-2019.md), §4.1):

| Code | Chain as described |
|---|---|
| Cosmos++ | "2D" scheme of Noble et al. (2006); a 5D numerical inversion as backup; then the entropy |
| ECHO | 3D scheme of Bucciantini & Del Zanna (2013); then the 1D scheme of Porth et al. (2017); then the entropy; then a floor reset with zero Eulerian velocity and unchanged field |
| HARM-Noble | "2D" then "1D_W" of Noble et al. (2006); the entropy replaces the energy when the solve fails, gives unphysical primitives, or the internal energy density falls below $10^{-2}$ times the squared fluid-frame field |
| BHAC | the advected entropy whenever the plasma beta is below $10^{-2}$ |
| [H-AMR](/software/h-amr.md) | the advected entropy as backup |
| iharm3D | failed cells replaced by an average over a neighbour stencil |
| IllinoisGRMHD | conserved variables violating physicality inequalities adjusted before a Noble-type solve (Etienne et al. 2012) |

* The Noble et al. two-unknown scheme of Siegel et al.'s table above thus
  runs inside two evolution codes (Cosmos++, HARM-Noble), always with
  fallbacks behind it. As in the batch-3 code papers, no failure rates,
  tolerances or timings are reported.
* Several chains end in the advected entropy, the relativistic analogue of
  the [dual-energy formalism](/methods/dual-energy-formalism.md) switch,
  which Kastaun et al. (2021) do not propose (above). Others end in
  neighbour averaging or a floor reset; see
  [density and pressure floors](/methods/numerical-floors.md).

## Later uses (batch 10)

**Athena++ in 2016: Noble 1D_W, dated.** The In codes section records
that [Athena++](/software/athena-plus-plus.md) inverts with the Newman &
Hamlin (2014) root-find (Stone et al. 2020, §4). The method paper of its
GRMHD module, [White et al. (2016)](/sources/white-2016.md), §3.1, uses a
scheme "based on" the 1D_W scheme of Noble et al. (2006) instead.
* **GR.** Primitives are $\rho$, $p$ and the normal-observer spatial
  velocity, which "describe subluminal motion no matter what values they
  have"; Newton–Raphson solves for $\rho h_{\mathrm{rel}}W^2$; hydro uses
  the same procedure with zero field.
* **SR.** MHD uses Newton–Raphson in the same variable, as Mignone &
  McKinney (2007), but on the residual of the conserved energy as a
  function of it; SR hydro solves the quartic in $\vert\mathbf v\vert$ in
  closed form (Schneider et al. 1993; eqs. 17–19), a non-iterative
  inversion absent from the schemes compared above.
* **Failure handling.** Density and pressure floors and a Lorentz-factor
  ceiling "often chosen to be 100"; out-of-range primitives are moved to
  the nearest admissible values; a non-converged iteration sets the
  floors and the cell's conserved variables are recomputed. No entropy
  fallback is described, unlike several chains of the batch-4 table.

The two Athena++ statements describe different epochs of the code (2016
and 2020); neither paper states when the inversion changed. This dates
the In codes line; it contradicts nothing. With this, the 1D_W scheme has
run inside a third evolution code besides HARM-Noble's chain (batch 4).

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
4. [Shankar et al. (2023)](/sources/shankar-2023.md), §II C (arXiv v2).
5. [Stone et al. (2026)](/sources/stone-2026.md), §§3.5–3.6, Table 2,
   Figs. 10, 13 (arXiv v1).
6. [Porth et al. (2019)](/sources/porth-2019.md), §4.1 (arXiv v2).
7. [White et al. (2016)](/sources/white-2016.md), §3.1, eqs. 16–19.
