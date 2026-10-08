---
type: Definition
title: "Modified wavenumber (dispersion and dissipation analysis)"
description: "The Fourier symbol of a discrete first-derivative operator: applied to e^{ikx} it returns i·ξ̃(ξ)/h; Re ξ̃ against ξ = kh measures dispersion and Im ξ̃ dissipation, the standard tool for judging capturing schemes for turbulence."
status: established
aliases: [modified wavenumber, transfer function, spectral resolution, ADR analysis]
tags: [spectral-analysis, dispersion, dissipation, definition]
timestamp: 2026-10-08T00:00:00Z
---

# Modified wavenumber

For a linear scheme $\partial_x f \approx \frac1h\sum_n a_n f_{i+n}$, a
Fourier mode $f = e^{ikx}$ gives $\frac1h\sum_n a_n e^{in\xi} = \frac{i}{h}\tilde\xi(\xi)$
with $\xi = kh$; the exact derivative has $\tilde\xi = \xi$. $\operatorname{Re}\tilde\xi$
sets the numerical phase speed (dispersion), $\operatorname{Im}\tilde\xi$
the decay (dissipation), which must have the stabilizing sign for the
upwind direction ([Martín et al. (2006)](/sources/martin-2006.md), §3;
[Pirozzoli (2002)](/sources/pirozzoli-2002.md), §2.2, as the "transfer
function"). Central schemes have no dissipation; upwind-biased ones do.

**Measures used in this corpus.**
* Lele's bandwidth-resolving efficiency: the largest $\xi/\pi$ for which
  the phase error stays below a threshold (1 %)
  ([Martín et al. (2006)](/sources/martin-2006.md); WENO-JS optimal
  stencil 0.35 at $r = 3$).
* For a nonlinear scheme the analysis applies to its linear (optimal-
  weight) scheme, an upper bound on its performance, or to the
  approximate dispersion relation (ADR) obtained numerically, which
  includes the adaptation (Pirozzoli, cited by
  [Fu, Hu & Adams (2016)](/sources/fu-2016.md)).
* A dispersion–dissipation relation (Hu, Tritschler, Pirozzoli and
  Adams, cited) sets the minimum dissipation needed to damp spurious
  high-wavenumber errors; Fu et al. use it as the optimization target and
  report that bandwidth-optimized WENO schemes violate it with
  anti-dissipation at low wavenumbers.

**Readings.** The fifth-order compact upwind flux resolves $\xi \le 2$
and concentrates dissipation at the highest wavenumbers
([hybrid compact-WENO](/methods/hybrid-compact-weno.md)); WENO-AO(7,5,3)
and AO(9,5,3) compare favourably with fourth- and sixth-order compact
schemes in dispersion ([adaptive-order WENO](/methods/weno-ao.md),
[Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §4.4); TENO
keeps its linear scheme's spectral properties to $\xi \approx 1.75$–$1.95$
depending on $C_T$ ([TENO](/methods/teno.md)).

# Citations

1. [Martín et al. (2006)](/sources/martin-2006.md), §3.
2. [Pirozzoli (2002)](/sources/pirozzoli-2002.md), §2.2.
3. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §§3.2, 4.
4. [Balsara, Garain & Shu (2016)](/sources/balsara-2016.md), §4.4.
