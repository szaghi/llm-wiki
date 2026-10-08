---
type: Source
title: "Mignone, Tzeferacos & Bodo (2010) — High-order conservative finite difference GLM-MHD schemes for cell-centered MHD"
description: "Third- and fifth-order conservative finite-difference schemes for multi-D ideal MHD with all variables cell-centred and GLM divergence cleaning, using characteristic global Lax–Friedrichs splitting and comparing WENO+3, LimO3, WENO-Z and MP5: fifth order costs 25–48% more than third but needs about a quarter of the points on smooth problems; MP5 ranks slightly ahead of WENO-Z."
resource: "doi:10.1016/j.jcp.2010.04.013"
source_kind: paper
authors: [Mignone A., Tzeferacos P., Bodo G.]
year: 2010
venue: "J. Comput. Phys. 229:5896-5920"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2010-JCP-Mignone-101016jjcp201004013.pdf"
tags: [mhd, finite-difference, divergence-free, weno, monotonicity]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

A finite-difference GLM-MHD framework in PLUTO with four interchangeable
reconstructions. Merged into the new
[hyperbolic divergence cleaning](/methods/hyperbolic-divergence-cleaning.md)
page, the WENO, WENO-Z, MP, energy-stable WENO, characteristic and
conservative-FD pages, and the new Alfvén-wave, field-loop and oblique
shock-tube benchmarks.

# Key claims

1. **GLM-MHD** (§2, eqs. 4–9): Dedner's scalar, nine waves, cleaning speed
   the largest the step allows, exact split damping with $\alpha_p$.
2. **FD scheme** (§3, eqs. 10–20): Shu–Osher flux form, characteristic
   splitting with domain-wide Lax–Friedrichs speeds per field and
   arithmetic-mean eigenvectors, SSP-RK3 (so overall third order in time).
   Global splitting is "particularly diffusive", less so at high order.
3. **Decoupled $(B_x, \psi_{\mathrm{GLM}})$ system** (§3.1, eqs. 21–24):
   constant eigenvectors, no local projection, then the $7\times7$ MHD
   system; 16 reconstructions per interface.
4. **Reconstructions** (§3.2): WENO+3 with Yamaleev–Carpenter weights and
   $\varepsilon = h^2$; LimO3 (Čada–Torrilhon); WENO-Z with $q = 1$,
   $\varepsilon = 10^{-40}$ (the printed $\beta_1$ in eq. 35 has a misprint);
   MP5 on flux point values.
5. **Cost** (§§4–5): relative CPU 1 : 0.98 : 1.46 : 1.31 (WENO+3 : LimO3 :
   WENO-Z : MP5) on the 3D Alfvén wave, similar elsewhere; equal accuracy
   on far coarser grids gives "almost two orders of magnitude" in 3D.
6. **Tests** (§4): circularly polarized Alfvén waves in 1D and 3D and their
   long-term decay; rotated Brio–Wu (2D) and Ryu–Jones (3D) shock tubes; 2D
   and new 3D MHD vortices; 2D and 3D field loops; Orszag–Tang on
   $[0, 1]^2$; MHD Kelvin–Helmholtz.

# Notation map

| Mignone et al. (2010) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\psi$, $c_h$, $c_p$, $\alpha_p$ | $\psi_{\mathrm{GLM}}$, $c_h$, $c_p$, $\alpha_p$ | |
| $\Gamma$ | $\gamma$ | |
| $\lambda^\kappa$, $\mathbf L^\kappa$, $\mathbf R^\kappa$, $\alpha^\kappa$ | $\lambda^{(p)}$, $\ell^{(p)}$, $r^{(p)}$, $\alpha$ | |
| $\hat{\mathbf F}(x)$, $\mathbf H$ | $\mathcal H$, its primitive | |
| $C_a$ (Courant number) | $\nu$ | registry $C_a$ is the ILW offset |
| $\alpha_l$ (weights), $\alpha$ (MP) | $\tilde\omega_k$, $\kappa$ | |
| $\Delta_{i+1/2}$, $d_i$ | $\Delta^1 f_i$, $\delta^2 f_i$ | |
| $\theta$, $\chi$, $\eta$ (LimO3) | (words) | |

# Pages created or updated

* Updated [Brio–Wu MHD shock tube](/benchmarks/brio-wu-shock-tube.md).
* Created [Circularly polarized (torsional) Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Conservative finite-difference (flux) formulation](/methods/conservative-finite-difference.md).
* Updated [Energy-stable WENO (ESWENO) with summation-by-parts boundary closures](/methods/energy-stable-weno.md).
* Created [Grid-oblique MHD shock tubes](/benchmarks/oblique-mhd-shock-tubes.md).
* Created [Hyperbolic (GLM) divergence cleaning](/methods/hyperbolic-divergence-cleaning.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Created [Magnetic field-loop advection](/benchmarks/field-loop-advection.md).
* Updated [Monotonicity-preserving (MP) limiting](/methods/monotonicity-preserving-limiter.md).
* Updated [Orszag–Tang vortex (2D MHD)](/benchmarks/orszag-tang-vortex.md).
* Created [PLUTO (astrophysical gas-dynamics and MHD code)](/software/pluto.md).
* Created [Self-similarity (scale invariance) of capturing schemes](/properties/self-similarity.md).
* Updated [WENO reconstruction (weighted ENO)](/methods/weno.md).
* Updated [WENO-Z](/methods/weno-z.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2010-JCP-Mignone-101016jjcp201004013.pdf` (arXiv:1001.2832v2, 17 April 2010, an author preprint, not the version of record; published as J. Comput. Phys. 229(17):5896–5920 (August 2010), doi:10.1016/j.jcp.2010.04.013, checked on Crossref): text extraction, all sections; eqs. 4–41 read from the page images. The Appendix A eigenvectors were read only from the garbled text layer and are not reproduced. Several printed reference venues are wrong (checked on Crossref and noted in the bibliography). Reference list: 54 entries.
