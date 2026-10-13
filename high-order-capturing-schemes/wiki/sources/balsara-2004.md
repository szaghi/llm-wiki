---
type: Source
title: "Balsara (2004) — Second-order-accurate schemes for magnetohydrodynamics with divergence-free reconstruction"
description: "Second-order unsplit Runge–Kutta Godunov schemes for MHD on a Yee-staggered mesh: divergence-free reconstruction of the face fields gives a unique zone-centred field, edge electric fields come from four Riemann problems per face without spatial averaging, with TVD, WENO-slope and multidimensional limiters, curvilinear and tetrahedral extensions, and a new MHD vortex test."
resource: "doi:10.1086/381377"
source_kind: paper
authors: [Balsara D.S.]
year: 2004
venue: "Astrophys. J. Suppl. Ser. 151:149-184"
local_file: "/home/stefano/papers/mosaic/high-order-capturing-schemes/2004-ApJS-Balsara-103847.pdf"
tags: [mhd, divergence-free, constrained-transport, reconstruction, staggered]
timestamp: 2026-10-08T00:00:00Z
---

# Summary

The paper names four open issues of divergence-free MHD schemes and
resolves them with a second-order divergence-free reconstruction and an
edge electric field built without spatial averaging. Merged into the new
[divergence-free reconstruction](/methods/divergence-free-reconstruction.md)
page and into the CT, Riemann-solver, characteristic, SSP and positivity
pages, and the rotor, blast, Alfvén-wave and vortex benchmarks.

# Key claims

1. **Issues** (§1): how to get the zone field; limiting the derived or the
   primal field; Powell's eighth wave, which "introduces magnetic
   monopoles"; edge fields from spatial averages.
2. **Edge fields** (§2, eqs. 2.10–2.13): four Riemann problems per face,
   one-sided fluxes at a single point next to each edge; the conserved
   update uses the same four fluxes and stays locally conservative.
3. **Reconstruction** (§3.1, eqs. 3.1–3.17): a quadratic field per
   component, four pointwise divergence constraints, closed-form
   coefficients, and the zone average of eq. 3.17, which is used for the
   pressure.
4. **Limiters** (§§3.2–3.5): fast primitive TVD (an empirical choice),
   characteristic TVD, $r = 2$ and $r = 3$ WENO slopes with direction-biased
   weights, a blended WENO, and a Barth-type multidimensional limiter.
   $r = 3$ is "too compressive" for genuinely nonlinear fields at strong
   shocks.
5. **Geometry** (§4, Appendices A–C): cylindrical and spherical volumetric
   coordinates and tetrahedra, with AMR prolongation formulas.
6. **Time** (§2, eqs. 2.5–2.6): second- and third-order Runge–Kutta. Eq.
   2.5 is labelled "TVD … the Heun scheme" but printed as the explicit
   midpoint rule, which the half-step of eq. 2.7 confirms. Recorded as
   printed.
7. **Tests** (§§6–7): a new MHD vortex (Tables 1–7); torsional Alfvén-wave
   decay at 9.462° (dissipation ordering of seven schemes); rotor; low-β
   blast (positive pressure credited to the reconstruction); a neutron-star
   disk–magnetosphere run. Accuracy hardly depends on the Riemann solver,
   dissipation does, and unsplit schemes beat dimensionally swept ones.

# Notation map

| Balsara (2004) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $a_0, a_x, a_{xx}, \dots$; $b_\cdot$, $c_\cdot$ | $\hat B_{x,0}, \hat B_{x,x}, \hat B_{x,xx}, \dots$; $\hat B_{y,\cdot}$, $\hat B_{z,\cdot}$ | |
| $B^\pm_x$ | face values of $B_x$ | |
| $\langle B_x\rangle_{\mathrm{vol\text{-}avg}}$ | $\langle B_x\rangle_i$ | |
| $\mathbf E$ (Gaussian units, factor $c$) | $\boldsymbol{\mathcal E}$ | registry $c$ is the sound speed |
| $\varepsilon$ (energy), $P$ | $E$, $p$ | |
| $C_\pm$, $\beta_\pm$ (WENO weights) | $d_k$, $\tilde\omega_k$ | unnormalized and direction-switched |
| $IS_k$ | $\beta_k$ | |
| $\tau_{i,j,k}$, $\psi$ (multi-D limiter) | $\theta$, (words) | |
| $\Delta x, \Delta y, \Delta z$ | $h_x, h_y, h_z$ | |

# Pages created or updated

* Updated [Approximate Riemann solvers as building blocks of capturing schemes](/methods/approximate-riemann-solvers.md).
* Created [Circularly polarized (torsional) Alfvén waves](/benchmarks/circularly-polarized-alfven-wave.md).
* Updated [Constrained transport for high-order capturing schemes (MHD)](/methods/constrained-transport.md).
* Created [Divergence-free reconstruction of face-centred magnetic fields](/methods/divergence-free-reconstruction.md).
* Updated [Isentropic vortex advection (smooth accuracy test)](/benchmarks/isentropic-vortex.md).
* Updated [Local characteristic decomposition](/methods/characteristic-decomposition.md).
* Updated [MHD blast wave in a low-β medium](/benchmarks/mhd-blast-wave.md).
* Updated [MHD rotor](/benchmarks/mhd-rotor.md).
* Updated [Positivity preservation (invariance of the admissible set)](/properties/positivity-preserving.md).
* Updated [TVD / strong-stability-preserving Runge–Kutta methods](/methods/ssp-runge-kutta.md).
* Updated [Notation registry](/notation.md): batch-6 registry extensions.
* Also cited on [HLL Riemann solver and wave-speed estimates](/methods/hll-riemann-solver.md) (created 2026-10-13).

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2004-ApJS-Balsara-103847.pdf` (doi:10.1086/381377, checked on Crossref: ApJS 151(1):149–184, March 2004; typeset journal article): text extraction, all sections; eqs. 2.5–2.13, 3.1–3.47, 6.1–6.5, 7.1–7.4 and Tables 1–7 read from the page images. Curvilinear volume averages, momentum equations and Appendices A–C are not reproduced. Reference list: 54 entries (ApJ style, mostly without titles).
