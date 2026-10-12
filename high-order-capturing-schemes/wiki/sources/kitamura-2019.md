---
type: Source
title: "Kitamura & Shima (2019) — Numerical experiments on anomalies from stationary, slowly moving, and fast-moving shocks"
description: "Joins Quirk's moving-shock test and the stationary-shock test into a map over shock Mach number and shock propagation Mach number, runs eight first-order fluxes on it, and shows that slowly moving shocks — slower than the post-shock signal speed, about 0.44 times the shock Mach number — are the most severe case for fluxes that capture shocks within one cell, so no single shock speed certifies robustness."
resource: "doi:10.2514/1.J057366"
source_kind: paper
authors: [Kitamura K., Shima E.]
year: 2019
venue: "AIAA J. 57:1763-1772"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2019-AIAAJ-Kitamura-1025141J057366.pdf"
tags: [riemann-solver, shock-instability, ausm, benchmark]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

A Note with no abstract and a purely experimental approach. Kitamura &
Shima sweep the shock Mach number $M_s \in \{1.5, 3, 6, 10\}$ against the
propagation Mach number $M_{\mathrm{prop}} \in \{0, 0.5, 1, 1.5, 3, 6, 10\}$
on Quirk's $800\times20$ grid with a $10^{-3}$ odd–even perturbation. The
fluxes are Roe with an entropy fix, van Leer, AUSM+-up, SLAU, LDFSS,
AUSMPW+, RoeM2 and SLAU2, all first order, run for 400 steps at CFL 0.4.
A post-shock signal Mach number separates slowly moving shocks, which
downstream noise can catch, from fast ones. Merged into
[numerical shock instability](/definitions/numerical-shock-instability.md),
the [slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md),
[Quirk's test](/benchmarks/quirk-odd-even-test.md) and the
[stationary normal shock](/benchmarks/stationary-normal-shock.md).

# Key claims

1. **No single speed certifies a flux** (§§I, IV.B, V). Quirk's
   moving-shock test "does not support the robustness of a numerical flux
   for a stationary shock, in a strict sense". Citing earlier work, "any
   flux functions including flux-vector-splitting (FVS) by Van Leer can
   generate carbuncles".
2. **Signal Mach number** (§III.B, eqs. 7–10, from the page image).
   $M_{\mathrm{sig}}(M_s)$ is the post-shock over the pre-shock sound
   speed from the Rankine–Hugoniot ratios. It tends to
   $\sqrt{2\gamma(\gamma-1)}\,M_s/(\gamma+1) \approx 0.44\,M_s$ for
   $\gamma = 1.4$. Below it, downstream noise can catch up with the shock;
   the neglected convection makes it a lower bound.
3. **Four groups for sharp-capturing fluxes** (§IV.B, §V).
   * Stationary shocks: no grid-perturbation influence, and a "comfortable"
     shock location per flux.
   * Slowly moving shocks, $0 < M_{\mathrm{prop}} < 0.44\,M_s$: "the most
     severe case".
   * Fast shocks: less prone, with mixed results.
   * Weak shocks, $M_s < 2$: "usually stable".
4. **Flux dependence** (§IV.B).
   * Roe, AUSM+-up and LDFSS capture shocks within one cell and are
     sensitive to shock speed.
   * SLAU, van Leer, AUSMPW+, RoeM2 and SLAU2 spread the shock over a few
     cells or carry multidimensional dissipation, and are insensitive.
   * SLAU is less stable at stationary than at moving shocks, the
     opposite of AUSM+-up.
5. **Roe map** (§IV.A, Fig. 9). Carbuncles for every
   $M_{\mathrm{prop}}$ at $M_s = 10$, for $M_{\mathrm{prop}} \le 6$ at
   $M_s = 6$, oscillatory for $M_{\mathrm{prop}} \le 3$ at $M_s = 3$, and
   stable at $M_s = 1.5$.
6. **Perturbation size** (§IV.C, Fig. 17). With $\epsilon_{\mathrm g} = 10^{-6}$
   or 0, Roe is unstable only at the stationary $M_s = 6$ and 10 points.
   $10^{-3}$ is "a good value to check the occurrence of shock anomalies
   in a realistic time".
7. **A tension with earlier results, explained.** Here AUSMPW+ is stable
   and SLAU2 shows slight growth, the opposite of the authors' unperturbed
   tests. They attribute this to AUSMPW+'s multidimensional pressure
   weight acting on perturbed grids (§IV.B).
8. **Order** (§II.B). Everything is first order. Citing earlier work, it
   says second order produces more post-shock oscillation from moving
   shocks and fewer carbuncles from stationary ones, depending on the
   limiter. It recommends SLAU2 with minmod for now (§V).

# Notation map

| Kitamura & Shima (2019) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\mathbf Q$; $\mathbf E$, $\mathbf F$ | $u$; components of $\mathbf f$ | |
| $E$ (per unit mass), $H$ | $E/\rho$; $(E + p)/\rho$ | registry $E$ is a density |
| $u$, $v$ | $v_x$, $v_y$ | |
| $a_L$, $a_R$ | $c$ post-shock, $c$ pre-shock | $L$ is post-shock here |
| $M$ (shock intensity) | $M_s$ | |
| $M_s$ (shock propagation) | $M_{\mathrm{prop}}$ | collides with registry $M_s$ |
| $M_{\mathrm{signal}}$ | $M_{\mathrm{sig}}$ | |
| $\varepsilon$ (shock location) | $\epsilon_{\mathrm{sh}}$ | |
| $\epsilon_g$ | $\epsilon_{\mathrm g}$ | |
| CFL | $\nu$ | |

# Pages created or updated

* Created [Numerical shock instability](/definitions/numerical-shock-instability.md), [Slowly moving shock anomaly](/definitions/slowly-moving-shock-anomaly.md), [Quirk's odd–even decoupling test](/benchmarks/quirk-odd-even-test.md), [Stationary normal shock test](/benchmarks/stationary-normal-shock.md), [Cures for numerical shock instability](/methods/shock-instability-cures.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (AUSM-family robustness; `Contradictions` on HLLE).
* Updated [Notation registry](/notation.md): $M_{\mathrm{prop}}$, $M_{\mathrm{sig}}$, $\epsilon_{\mathrm{sh}}$, $\epsilon_{\mathrm g}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2019-AIAAJ-Kitamura-1025141J057366.pdf`.
   * **Version.** The revised author manuscript (R1, Word file of 31
     October 2018, revisions highlighted), 23 pages, from the Yokohama
     National University repository. It is not the typeset Note.
   * **Identity.** doi:10.2514/1.J057366, checked on Crossref: AIAA J.
     57(4):1763–1772, April 2019, authors Kitamura and Shima.
   * **How it was read.** Text extraction, all sections. Eq. 10b and
     Figs. 9 and 12 were read from the page images.
   * **Not reconciled.** The text mentions a point $(M_s, M_{\mathrm{prop}}) = (3, 2)$
     that is not in Table 1.
   * **Reference list:** 33 entries.
