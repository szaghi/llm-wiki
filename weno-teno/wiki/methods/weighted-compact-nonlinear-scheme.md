---
type: Method
title: "Weighted compact nonlinear schemes (WCNS)"
description: "WCNS are finite-difference shock-capturing schemes in three steps — nonlinear node-to-interface interpolation of the variables, a two-point flux at the interfaces, and high-order compact interface-to-node flux differencing; this page records the family as the chunk-1 sources recall it, its TENO-weighted members (TCNS, WCNS-T), its relation to the alternative WENO formulation, and its stated weaknesses."
status: established
aliases: [WCNS, WCNS-Z, WCNS-JS, TCNS, targeted compact nonlinear scheme, WCNS-T, HWCNS]
tags: [compact-scheme, finite-difference, weno, teno, numerical-flux]
timestamp: 2026-10-21T00:00:00Z
---

# Weighted compact nonlinear schemes (WCNS)

The **weighted compact nonlinear scheme** of Deng and Zhang (as recalled by
[Fu (2023)](/sources/fu-2023.md), §3.7) is a finite-difference scheme built in
three steps:

1. a nonlinear (WENO-weighted) **interpolation** of the variables from the nodes
   $x_i$ to the interfaces $x_{i+1/2}$, giving $u^\pm_{i+1/2}$;
2. evaluation of an **interface flux** $h(u^-_{i+1/2},u^+_{i+1/2})$, e.g. a
   Riemann solver;
3. high-order **compact** (implicit) **interface-to-node differencing** of the
   interface fluxes to obtain $\partial_xf$ at the nodes.

It shares step 1 and 2 with the
[alternative WENO formulation](/methods/alternative-weno.md), which reaches high
order by explicit even-derivative corrections instead of compact differencing;
[Ye et al. (2022)](/sources/ye-2022.md) (§1) state, as recalled, that AFWENO "is
similar to WCNS and is equivalent to the HWCNS scheme under specific parameters"
(HWCNS is cited to a Deng et al. AIAA conference paper). For
[AFTENO](/methods/afteno.md), Ye et al. (§1, §5) credit this
interpolation-plus-flux structure with the freedom to use any monotone or
Riemann-solver flux and to interpolate conserved, primitive or characteristic
variables.

## Members recalled in the sources

- **WCNS-JS and WCNS-Z**: interpolation weighted with Jiang–Shu or WENO-Z
  weights; WCNS-Z beats WCNS-JS ([Fu (2023)](/sources/fu-2023.md), §3.7).
- **TCNS** (targeted compact nonlinear schemes): WCNS with the
  [TENO](/methods/targeted-eno.md) weighting (incremental stencils, sharp
  cut-off). TCNS "clearly beat" WCNS-Z; TCNS6 is better than seventh- and
  ninth-order WCNS-Z on the Shu–Osher problem, and TCNS is insensitive to the
  definition of the global indicator $\tau_K$, which mainly affects cost; a TCNS
  with adaptive dissipation exists (Fu 2023, §3.7, §4.1; see
  [adaptive TENO](/methods/adaptive-teno.md)).
- **WCNS-T** (Hiejima): fifth-, seventh-, ninth- and eleventh-order WCNS with TENO
  weighting (Fu 2023, §3.7; also cited by Ye et al., §1).
- **Learned variants**: WCNS3-NN and WCNS3-MR-NN, to which Huang et al. claim
  their diagram-fitting method applies ([Huang et al. (2026)](/sources/huang-2026.md),
  §7; see [learned WENO weights](/methods/learned-weno-weights.md)).

## Stated weaknesses and neighbours

- Fu (2023, §3.7) names "lack of conservation" as the main flaw of WCNS. This is a
  recalled judgement; the chunk-1 sources do not show the mechanism.
- **CRWENO** (Ghosh and Baeder, as recalled by Fu 2023, §3.7): compact
  reconstruction WENO, with lower dissipation than WENO at low and moderate
  wavenumbers and higher dissipation at aliased wavenumbers; a TENO variant
  exists.

## Qualifications

This page is a recollection page: no chunk-1 source derives a WCNS, and all
performance statements are relayed from cited works. It earns its place because
two sources place AFWENO and AFTENO relative to it and the TENO review lists its
TENO-weighted members; formulas belong to a later ingested WCNS source.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.7: three-step WCNS, WCNS-Z, TCNS, WCNS-T, CRWENO, conservation remark.
- [Ye et al. (2022)](/sources/ye-2022.md) — §1, §5: AFWENO similar to WCNS, equivalent to HWCNS; WCNS-T cited.
- [Huang et al. (2026)](/sources/huang-2026.md) — §7: WCNS3-NN, WCNS3-MR-NN.
