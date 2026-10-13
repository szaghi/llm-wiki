---
type: Source
title: "Pirozzoli (2002) — Conservative hybrid compact-WENO schemes for shock-turbulence interaction"
description: "A conservative fifth-order compact upwind flux (tridiagonal) for smooth regions, switched to WENO5/WENO7 near discontinuities by a density-difference sensor; Fourier and eigenvalue stability analyses; better resolution than WENO and compact-ENO hybrids at lower cost."
resource: "doi:10.1006/jcph.2002.7021"
source_kind: paper
authors: [Pirozzoli S.]
year: 2002
venue: "J. Comput. Phys. 178:81-117"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2002-JCP-Pirozzoli-101006jcph20027021.pdf"
tags: [compact-scheme, hybrid, turbulence, spectral-resolution]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Improves the Adams–Shariff hybrid compact-ENO approach with a conservative
compact scheme (easier coupling, fewer oscillations), a tridiagonal rather
than pentadiagonal solve, and WENO instead of ENO at discontinuities.
Merged into [hybrid compact-WENO](/methods/hybrid-compact-weno.md) and
[modified wavenumber](/definitions/modified-wavenumber.md).

# Key claims

1. **Conservative compact upwind family** (§2.1): coefficients from Taylor
   matching; the unique fifth-order tridiagonal member (eq. 8); explicit
   fifth- and seventh-order upwind schemes (eqs. 9–10) are WENO5/7's
   linear limits.
2. **Spectral resolution** (§2.2, Fig. 1): waves at three points per
   wavelength; dissipation at high wavenumbers only.
3. **Boundary closures and stability** (§§2.2–2.3): eigenvalues of the
   semi-discrete matrix; von Neumann analysis with RK4.
4. **Switch** (§3): undivided density differences above $\vartheta$; H5,
   H7; tests on Harten's linear case.
5. **Euler** (§§4–5): LDLF/HDLF splittings, density-based indicators;
   Burgers, Shu–Osher, Mach 8 shock–vorticity, 3D shock–turbulence
   interaction (DNS-like spectra with a cutoff at 3 points per wavelength).

# Notation map

| Pirozzoli (2002) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $v$, $\tilde v_{i+1/2}$ | $f$, $\hat f_{i+1/2}$ | |
| $u(x)$, $U(x)$ | $\mathcal{H}$, its primitive | |
| $\hat k$, $Z(\hat k)$ | $\xi$, $\tilde\xi(\xi)$ | |
| $\sigma$ (switch) | $\vartheta$ | |
| $\epsilon$ | $\varepsilon$ | |
| $\lambda$ (splitting) | $\alpha$ | |

# Pages created or updated

* Updated [Shu–Osher shock/entropy-wave interaction](/benchmarks/shu-osher-problem.md).
* Created [Modified wavenumber (dispersion and dissipation analysis)](/definitions/modified-wavenumber.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Created [Hybrid compact-WENO schemes](/methods/hybrid-compact-weno.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Notation registry](/notation.md): batch-2 registry extensions.
* Also cited on [Compact-reconstruction WENO (nonlinear compact schemes)](/methods/compact-reconstruction-weno.md).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2002-JCP-Pirozzoli-101006jcph20027021.pdf` (doi:10.1006/jcph.2002.7021): text extraction, all sections; the compact coefficients and closures (eqs. 6–17) are illegible in the text layer and not reproduced. Reference list: 50 entries.
