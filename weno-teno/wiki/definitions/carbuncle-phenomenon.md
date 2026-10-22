---
type: Definition
title: "Carbuncle phenomenon"
description: "The carbuncle is a numerical instability that low-dissipation approximate Riemann solvers such as HLLC and Roe can develop near strong shocks; the bundle's shock-capturing sources avoid it by switching to the more dissipative, carbuncle-free HLL solver at strong shocks, and a shock-fitting moving DG method reports no carbuncle on hypersonic bow shocks."
status: established
aliases: [carbuncle problem, carbuncle instability, shock instability of low-dissipation Riemann solvers]
tags: [riemann-solver, numerical-flux, benchmark]
timestamp: 2026-10-22T00:00:00Z
---

# Carbuncle phenomenon

The **carbuncle phenomenon** is the numerical instability that some approximate Riemann
solvers develop in the vicinity of strong shock waves. In the sources of this bundle it is
identified by the solvers that exhibit it and by the remedy, not by a mechanism:
[Fu (2023)](/sources/fu-2023.md) (§3.6) states that "the HLLC and Roe solvers may induce
carbuncle problem in proximity to strong shockwaves with low numerical dissipation whereas
the HLL solver is free from carbuncle problem but featuring substantially larger
dissipation", and concludes that "there is no unique Riemann solver capable of handling all
Mach numbers". [Huang et al. (2026)](/sources/huang-2026.md) (§6.7) likewise state that "the
HLLC solver is known to exhibit numerical instabilities in the presence of strong shock
waves".

The defining trade-off is therefore between the resolution that a low-dissipation solver
gives to contacts and shear layers and the robustness that the more dissipative HLL solver
gives at strong shocks ([HLL-family solvers](/methods/hll-riemann-solvers.md),
[numerical dissipation](/definitions/numerical-dissipation.md)).

## Remedies used in the sources

- **Solver switching by smoothness.** The low-dissipation finite-volume TENO recalled by
  [Fu (2023)](/sources/fu-2023.md) (§3.6, Eq. (30)) uses a low-dissipation flux (HLLC, or the
  central flux for turbulence) where both full reconstruction stencils are flagged smooth by
  the TENO cut-off and the HLL flux otherwise, "to avoid the carbuncle problem while the HLLC
  flux [is] imposed for smooth flows to resolve the fine-scale structures"
  ([targeted ENO](/methods/targeted-eno.md)).
- **HLL for the strong-shock test case.** [Huang et al. (2026)](/sources/huang-2026.md)
  (§6.7) run their compact-stencil reconstructions with HLLC by default but switch to HLL for
  the Mach-10 [double Mach reflection](/benchmarks/double-mach-reflection.md) "to mitigate
  the carbuncle phenomenon".

- **Fitting the shock instead of capturing it.** In the moving discontinuous
  Galerkin method MDG+ICE of [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md)
  the bow shock is a mesh face located by the weakly enforced interface
  ([Rankine–Hugoniot](/definitions/rankine-hugoniot-condition.md)) condition,
  and the interior flux is the plain central average, with no Riemann solver.
  On the steady Mach 8 (315 elements) and Mach 15 (497 elements) flows past a
  half cylinder, computed with linear elements, the authors observe "no shock
  instabilities or carbuncle phenomenon" (§IV.E, Fig. 28). The evidence is the
  figure alone; no shock-capturing comparison is run. See
  [implicit shock tracking](/methods/implicit-shock-tracking.md).

## Qualifications

- None of the sources describes the carbuncle's form or its mechanism; this page records
  only what they state. Fu (2023) cites a dedicated reference for it and, among its references,
  a rotated-hybrid carbuncle-free Riemann solver (Nishikawa & Kitamura), which the review
  mis-cites as the Rusanov solver (§3.6).
- Luo, Absillis & Nourgaliev's Fig. 28 caption gives Mach 8 and 18, the text Mach 8 and 15;
  the page follows the text.

# Citations

- [Fu (2023)](/sources/fu-2023.md) — §3.6 (Eq. (30), Fig. 9).
- [Huang et al. (2026)](/sources/huang-2026.md) — §6.7 (Fig. 12).
- [Luo, Absillis & Nourgaliev (2021)](/sources/luo-2021.md) — §3.3, §IV.E (Fig. 28; author manuscript).
