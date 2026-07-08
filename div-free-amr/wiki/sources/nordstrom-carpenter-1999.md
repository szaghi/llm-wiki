---
type: Source
title: "Nordström & Carpenter (1999) — High order finite difference methods, multidimensional linear problems and curvilinear coordinates"
description: "SBP-SAT boundary and interface conditions for multi-block curvilinear grids: conservative, strictly and strongly stable schemes conditional on metric conditions."
resource: "NASA/CR-1999-209834 (ICASE Report 99-54)"
source_kind: report
authors: [Nordström J., Carpenter M.H.]
year: 1999
venue: "NASA/CR-1999-209834, ICASE Report 99-54"
local_file: "~/papers/mosaic/div-free-amr/1999-ICASE-Nordstrom-NASA-CR-1999-209834.pdf"
tags: [sbp, sat, interface-conditions, curvilinear, multi-block, stability]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Extends the [SBP](/definitions/summation-by-parts.md) energy-method
framework from 1D constant-coefficient problems to **multidimensional
linear problems in curvilinear coordinates on multi-block grids**: boundary
and *interface* conditions are imposed weakly by the
[SAT penalty technique](/methods/sbp-sat.md), yielding schemes that are
conservative and strictly/strongly stable — **provided certain metric
conditions are met**. The variable-coefficient/curvilinear setting forces a
norm that depends on the Jacobian of the coordinate transformation, and the
analysis quantifies what survives. (No DOI exists for this report; the NASA
report number is the permanent identifier. Journal versions followed; not
in this corpus.)

# Key claims

1. **Interfaces with matching gridlines**: the block-interface treatment
   (their §4.3) assumes coordinate lines match across the interface (their
   eq. 4.34 equates the tangential metric terms from both sides); the SAT
   penalties are applied to the *fluxes*, whose normal components are
   identified as the continuous quantities across the interface. This is
   the **conforming** case — nonconforming (2:1-type) SBP interfaces are
   later work, not in this report.
2. **Flux- vs variable-interface conditions** (§4.3.2): penalizing flux
   continuity degenerates as the wave speed $a \to 0$ (the advective flux
   carries no information), while variable conditions
   ($u = v$, $u_x = -v_x$ after reflection) stay well behaved — a concrete
   warning about *which* continuity to penalize at interfaces.
3. **Metric conditions as the price of curvilinearity**: with
   Jacobian-weighted norms, strict stability and conservation hold only
   under conditions on the discrete metric terms — the variable-coefficient
   analog of the freestream/metric-identity discipline; on non-smooth
   meshes the metric derivatives themselves are the hazard.
4. **Accuracy**: numerical experiments confirm the theory — with
   boundary/interface closures one order lower than the interior,
   convergence between fifth and sixth order is observed for the
   sixth-order interior scheme, consistent with the theory they cite.

# Notation map

| Nordström & Carpenter | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| SBP operators $P^{-1}Q$ | $\mathsf{H}^{-1}\mathsf{Q} = \mathsf{D}_1$ | their $P$ is the norm — renamed $\mathsf{H}$ (registry collision rule) |
| SAT penalty terms | — | named technique; see method page |
| $\xi, \eta$ metric terms $(x_\xi, y_\xi, \dots)$ | curvilinear mapping derivatives | Jacobian enters the norm |
| matching gridlines (4.34) | conforming block interface | *not* a 2:1 refinement interface |

# Pages created or updated

* Created [SBP-SAT technique](/methods/sbp-sat.md).
* Updated [Summation by parts (SBP)](/definitions/summation-by-parts.md) (multi-block/curvilinear extension; metric conditions).

# Citations

1. `~/papers/mosaic/div-free-amr/1999-ICASE-Nordstrom-NASA-CR-1999-209834.pdf` (NASA/CR-1999-209834) — text extraction, 24 pp. + figures.
