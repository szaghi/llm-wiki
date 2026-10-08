---
type: Source
title: "Berta, Mignone, Bugli & Mattia (2024) — A 4th-order accurate finite volume method for ideal classical and special relativistic MHD based on pointwise reconstructions"
description: "Fourth-order finite volume with constrained transport for classical and relativistic MHD in PLUTO: averages converted to point values by the Δ/24 Laplacian, MP5 or WENO-Z interpolation of point values with new linear weights, one Riemann problem per face, fourth-order upwind CT, eSSPRK(5,4), and detector-driven order reduction; exactly fourth order on Alfvén waves."
resource: "doi:10.1016/j.jcp.2023.112701"
source_kind: paper
authors: [Berta V., Mignone A., Bugli M., Mattia G.]
year: 2024
venue: "J. Comput. Phys. 499:112701"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2024-JCP-Berta-101016jjcp2023112701.pdf"
tags: [mhd, relativistic, finite-volume, fourth-order, constrained-transport]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

Builds on McCorquodale–Colella and Felker–Stone but reconstructs point
values. Merged into the fourth-order FV (new section), CT (new section on
upwind CT), FV-reconstruction, WENO-Z, MP, energy-stable WENO,
Riemann-solver and SSP pages, the [PLUTO](/software/pluto.md) page, and
the Alfvén-wave, field-loop, oblique shock-tube, vortex, Orszag–Tang,
blast and shock–cloud benchmarks.

# Key claims

1. **Conversions** (§3.1, eqs. 16–21): $\tfrac1{24}$ undivided Laplacians
   between averages and point values, on cells and faces; the zone field
   from the faces by a four-point formula (eq. 22).
2. **Pointwise reconstruction** (§3.2, eqs. 23–28): MP5 on the five-point
   interpolant; WENO-Z with $d = (\tfrac1{16}, \tfrac58, \tfrac5{16})$ and
   $\varepsilon = 10^{-40}$; WENO3 in Yamaleev–Carpenter form with
   $d = (\tfrac34, \tfrac14)$, $\varepsilon = h^2$. Eq. 27 appears to have an
   index typo (a compiler's check). "To the extent of our knowledge" the
   first pointwise reconstruction in FV.
3. **Fluxes** (§§3.2–3.3, eqs. 29–30): one Riemann problem per face,
   against four for two-point Gauss quadrature in 3D; Roe, HLL, HLLC,
   HLLD, Lax–Friedrichs or GFORCE.
4. **Time** (eq. 31): eSSPRK(5,4) with all coefficients printed.
5. **Order reduction** (§3.4, eqs. 33–37): Jameson's or a new
   derivative-ratio detector; the threshold is never given a value, and
   eq. 37 appears to have a typo.
6. **Upwind CT** (§4, eqs. 38–40, Appendix B): Mignone–Del Zanna edge
   fields with a $\tfrac1{24}$ edge correction; a new GFORCE average for
   RMHD; typos of the earlier paper corrected.
7. **Cost model** (§5.3): fourth order on about $34^3$ matches second order
   on $512^3$ at about $10^4$ times less time.
8. **Tests** (§5): rotated shock tubes; MHD vortex and a new RMHD vortex;
   circularly polarized Alfvén waves (orders 4.00); field loops; current
   sheet; Orszag–Tang; 3D blasts (energy correction needed beyond a
   moderate field); 3D shock–cloud.

# Notation map

| Berta et al. (2024) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\langle Q\rangle_c$, $\hat Q_{\mathbf x_f}$, $\bar Q_{\mathbf x_e}$ | $\langle w\rangle_i$, $\langle w\rangle_{i+1/2}$, edge average | the paper's hat and bar differ from the registry's |
| $\Delta$, $\Delta^x_\perp$ (undivided) | $h^2\Delta_h$, $h^2\Delta^\perp_h$ | |
| $V$, $\mathcal V(\cdot)$ | $\mathbf W$, $\mathbf W(\cdot)$ | |
| $\alpha_l$, $d_l$, $\beta_l$ | $\tilde\omega_k$, $d_k$, $\beta_k$ | |
| $\mathscr C$ | $\nu$ | |
| $\Gamma$ | $\gamma$ | the paper's $\gamma$ is the Lorentz factor |
| $\theta_c$, $\eta_c$ | $1 - \mathcal B_i$, (words) | |

# Pages created or updated

* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Created [Circularly polarized (torsional) Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Updated [Energy-stable WENO (ESWENO) with summation-by-parts boundary closures](/methods/energy-stable-weno.md).
* Updated [Fourth-order finite-volume method with average–point conversions](/methods/fourth-order-finite-volume.md).
* Created [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Created [Magnetic field-loop advection](/benchmarks/field-loop-advection.md).
* Updated [MHD blast wave in a low-β medium](/benchmarks/mhd-blast-wave.md).
* Updated [Monotonicity-preserving (MP) limiting](/methods/monotonicity-preserving-limiter.md).
* Updated [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Created [PLUTO (astrophysical gas-dynamics and MHD code)](/software/pluto.md).
* Updated [Reconstruction from cell averages](/methods/finite-volume-reconstruction.md).
* Updated [Shock–cloud interaction (MHD and relativistic MHD)](/benchmarks/shock-cloud-interaction.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [WENO-Z](/methods/weno-z.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2024-JCP-Berta-101016jjcp2023112701.pdf` (arXiv:2310.11831v4, 18 December 2023, a preprint, not the version of record; published as J. Comput. Phys. 499:112701 (February 2024), doi:10.1016/j.jcp.2023.112701, checked on Crossref): text extraction, all sections; eqs. 16–40 read from the page images. The descriptions of the fallback order disagree (first, second), and CFL numbers are missing for several tests. Reference list: 85 entries.
