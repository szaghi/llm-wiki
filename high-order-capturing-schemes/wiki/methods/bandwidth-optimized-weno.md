---
type: Method
title: "Symmetric and bandwidth-optimized WENO (WENO-SYMOO, WENO-SYMBO)"
description: "Martín–Taylor–Wu–Weirs modification of WENO-JS for turbulence DNS: an added downwind candidate makes the stencil set symmetric, and the optimal weights are chosen either for maximum order (2r, non-dissipative) or for bandwidth by minimizing a spectral error integral."
status: established
aliases: [WENO-SYM, WENO-SYMOO, WENO-SYMBO, bandwidth-optimized WENO]
tags: [weno, low-dissipation, turbulence, spectral-resolution]
timestamp: 2026-10-08T00:00:00Z
---

# Symmetric and bandwidth-optimized WENO

**Motivation** ([Martín et al. (2006)](/sources/martin-2006.md)). WENO-JS
is too dissipative for DNS of compressible turbulence. Its dissipation
has two sources — the adaptation mechanism and the optimal (linear)
stencil; this work targets the second. The WENO-JS candidates are
biased upwind about $x_{i+1/2}$, so their optimal stencil is
dissipative.

**WENO-SYM.** One more candidate stencil, fully downwind, makes the set
of $r + 1$ candidates symmetric. To prevent instability, the downwind
stencil's indicator is constrained so that its normalized weight never
exceeds the smallest of the others' (described in words; the constraint
formula is not legible in the copy read).
* **SYMOO** (order-optimized): optimal weights of order $2r$, no
  dissipation at all; found to be unstable near contact surfaces.
* **SYMBO** (bandwidth-optimized): optimal weights minimizing an
  integrated error over scaled wavenumbers, phase and amplitude errors
  weighted equally, with a deliberate dissipative bias at high
  wavenumbers and the low wavenumbers weighted more; candidate
  coefficients keep $r$-th order. Lele's bandwidth-resolving efficiency
  index (1 % phase error) rises from 0.35 to 0.49 at $r = 3$ and from
  0.42 to 0.56 at $r = 4$
  ([modified wavenumber](/definitions/modified-wavenumber.md)). The
  error function and its parameters were found by trial and error —
  "subjective, but not arbitrary".

**Results** ($\varepsilon = 10^{-10}$; $q = 1$ unless stated, $q = 2$
being more dissipative). Sine advection at 8 points per wavelength:
SYMBO least dissipative, then WENO-JS $q = 1$, then $q = 2$. Shock tube:
at $r = 4$, WENO-JS $q = 1$ and SYMOO show dispersive density errors.
Shu–Osher (and a weak Mach 1.1 shock over 20 % density fluctuations, and
an oblique Shu–Osher at 22° and 45°): WENO-SYM resolves the extrema that
WENO-JS damps; no difference near the shock. Decaying isotropic
turbulence: at $M_t = 0.1$ the WENO schemes need $128^3$ where a
sixth-order Padé scheme converges at $64^3$; at $M_t = 1.5$ SYMBO gives a
$k^{-5/3}$ inertial range with shocklets; a Mach 2.32 turbulent boundary
layer agrees with experiment. The nonlinear (adaptation) dissipation is
left for future work.

**Later assessments.** [Hu, Wang & Adams (2010)](/sources/hu-2010.md):
SYMBO degenerates in order in smooth regions and SYMOO is unstable near
contacts even with moderate shocks; their WENO-CU6 includes a downwind
stencil without that instability
([central-upwind WENO](/methods/central-upwind-weno.md)).
[Fu, Hu & Adams (2016)](/sources/fu-2016.md): SYMBO-type optimizations
produce anti-dissipation in the low-to-intermediate wavenumber range and
fail their dispersion–dissipation relation ([TENO](/methods/teno.md)).

# Citations

1. [Martín et al. (2006)](/sources/martin-2006.md), §§1–8 and Appendix.
2. [Hu, Wang & Adams (2010)](/sources/hu-2010.md), §1.
3. [Fu, Hu & Adams (2016)](/sources/fu-2016.md), §§1, 4.1.
