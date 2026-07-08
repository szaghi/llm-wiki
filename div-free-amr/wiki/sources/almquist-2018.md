---
type: Source
title: "Almquist, Wang & Werpers (2019) — Order preserving interpolation for summation-by-parts operators at non-conforming grid interfaces"
description: "Restores full global convergence at nonconforming SBP interfaces for second-derivative PDEs via order-preserving interpolation pairs, circumventing the quadrature-order accuracy bound."
resource: "doi:10.1137/18M1191609"
source_kind: paper
authors: [Almquist M., Wang S., Werpers J.]
year: 2019
venue: "SIAM J. Sci. Comput. 41(2):A1201-A1227 (arXiv:1806.01931, 2018)"
local_file: "~/papers/mosaic/div-free-amr/2018-SISC-Almquist-10113718M1191609.pdf"
tags: [sbp, interpolation, nonconforming, coarse-fine-interface, second-derivative, accuracy]
timestamp: 2026-07-08T00:00:00Z
---

# Summary

Fixes the standing accuracy defect of nonconforming SBP interfaces for
PDEs with second derivatives: previous couplings via
[SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md)
"have been forced to accept a reduction of the global convergence rate by
one order" from interface truncation error. The root cause is a proven
bound — interpolation-operator accuracy is capped by the order of the
quadrature rule associated with the SBP norm, so for interior order $2p$
the pair accuracies satisfy $q_{u2v} + q_{v2u} \le 2p+1$ — which raising
the interpolation order cannot beat. The remedy: **order-preserving (OP)
interpolation operators**, which come in *two pairs*; each pair obeys the
bound, but deploying the pairs asymmetrically inside the SATs (the "good"
direction where the truncation bites) removes the interface penalty.
Existence is **proved for any two diagonal-norm SBP schemes, regardless of
the grid-point distributions along the interface**; numerical experiments
(Schrödinger, heat, second-order wave) confirm one order higher global
convergence than the Mattsson–Carpenter coupling.

# Key claims

1. **The accuracy bound**: interpolation accuracy is bounded by the SBP
   norm's quadrature order (their refs — Lundquist–Nordström and Wang et
   al. lines, corpus papers pending ingestion); best achievable split for
   interior order $2p$: one direction $p+1$, constrained jointly by
   $q_{u2v} + q_{v2u} \le 2p+1$.
2. **Two pairs beat one**: a single pair cannot escape the bound; two
   pairs — one more accurate coarse-to-fine, one more accurate
   fine-to-coarse — used in the right SAT slots yield largest local
   truncation error one order better, hence full global order.
3. **Unconditional existence** for diagonal-norm SBP schemes with any
   interface point distributions — the 2:1 case included, but the result
   is general nonconforming.
4. **Alternative rejected**: degree-preserving SBP operators with
   extra-high-order quadratures exist but have point-count-dependent
   boundary closures and unclear extension to variable-coefficient second
   derivatives; OP pairs need no new SBP operators.

# Notation map

| Almquist et al. | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $I_{u2v}, I_{v2u}$ (two pairs, superscripts $e$/$d$) | $I_{C2F}, I_{F2C}$ generalized to OP pairs | "e" = extra-accurate, "d" = dissipative-compatible |
| $q_{u2v} + q_{v2u} \le 2p+1$ | interpolation accuracy pair-bound | quadrature-order cap |
| $2p$ | interior order | diagonal norm |

# Pages created or updated

* Updated [SBP-preserving interpolation](/operators/sbp-preserving-interpolation.md) (accuracy bound; OP pairs restore full order).

# Citations

1. `~/papers/mosaic/div-free-amr/2018-SISC-Almquist-10113718M1191609.pdf` (doi:10.1137/18M1191609, Crossref-verified authorship) — text extraction, 33 pp.
