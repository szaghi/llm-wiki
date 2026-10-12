---
type: Source
title: "Edelmann et al. (2021) — Well-balanced treatment of gravity in astrophysical fluid dynamics simulations at low Mach numbers"
description: "Compares three well-balancing methods (Cargo–LeRoux extended to multi-D, α-β, deviation) with a low-Mach AUSM+-up flux in a second-order implicit finite-volume code over long 2D runs: α-β and deviation preserve hydrostatic states to machine precision and far beat Cargo–LeRoux, only the deviation method balances moving equilibria, and well-balanced runs with low-Mach fluxes can still grow perturbations in stable stratifications."
resource: "doi:10.1051/0004-6361/202140653"
source_kind: paper
authors: [Edelmann P.V.F., Horst L., Berberich J.P., Andrassy R., Higl J., Leidi G., Klingenberg C., Röpke F.K.]
year: 2021
venue: "Astron. Astrophys. 652:A53"
local_file: "~/papers/mosaic/high-order-capturing-schemes/2021-A&A-Edelmann-10105100046361202140653.pdf"
tags: [well-balanced, low-mach, gravity, source-terms]
timestamp: 2026-10-12T00:00:00Z
---

# Summary

The Seven-League Hydro (SLH) code is cell-centred, implicit and second
order, and here runs a low-Mach AUSM+-up flux. In it the paper compares
three [well-balancing](/properties/well-balanced.md) methods:
Cargo–LeRoux, extended here to multi-D; the α-β method; and the deviation
method. All three need the equilibrium known in advance. α-β and deviation
balance it to machine precision rather than to second order. The tests
are long 2D runs: hydrostatic atmospheres, a rising bubble, heated
convection under a stable layer with radiation pressure, and a Keplerian
disk. The paper contains no shocks and no reconstruction beyond unlimited
linear; its link to this bundle is flux design, through
[low-Mach-number fluxes](/methods/low-mach-number-fluxes.md) and their
interplay with exact steady-state preservation.

# Key claims

1. **Definition of well-balanced** (§4, eqs. 39–44). One forward Euler
   step from the discrete equilibrium must leave it unchanged. The mass
   and energy conditions hold automatically at zero velocity; the
   momentum condition requires the source to match the flux difference.
2. **Low-Mach AUSM+-up** (§3.2, eqs. 29–38, from the page images).
   * The split pressure and mass-flux form has pressure-velocity diffusion
     scaled by $\mu_{\mathrm{pc}}(2 - \mu_{\mathrm{pc}})$.
   * SLH gives the pressure-diffusion term its own cut-off, about
     $10^{-1}$ against $10^{-13}$, to avoid instabilities.
   * With well-balanced reconstruction the pressure diffusion acts only on
     the non-hydrostatic pressure.
3. **Cargo–LeRoux** (§4.1). A potential absorbs the source, and a modified
   pressure and energy turn the system into homogeneous Euler. In multi-D
   it is exact only if $\mathbf g$ is parallel to $\nabla\rho$, so the
   paper uses a horizontal average, which balances approximately. It
   needs a flux that preserves contacts.
4. **α-β** (§4.2, eqs. 58–66). Reconstruct density and pressure divided by
   known profiles, then multiply back at the faces. The source is written
   to cancel the flux difference exactly.
5. **Deviation** (§4.3, eqs. 67–72). Evolve $u - u^{\mathrm{eq}}$, with flux
   and source differences. It handles equilibria with non-zero velocity.
   It "can be applied in arbitrarily high order finite-volume codes", a
   claim cited from Berberich et al. and not tested here.
6. **Growth with low-Mach fluxes** (§5.1, App. A).
   * In 2D stable stratifications, every well-balanced run with low-Mach
     AUSM+-up grows exponentially from Mach about $10^{-13}$. The
     dissipative variant stays below $10^{-11}$.
   * The Miczek et al. (2015) and Li & Gu (2008) fluxes behave "similar"
     (no figure).
   * The growth is attributed to pressure–velocity decoupling, a
     hypothesis. 1D runs do not show it.
7. **Long runs are necessary** (§§5.1, 6). A test of two sound-crossing
   times would miss the growth.
8. **Gravitational energy** (§2.1). Including $\rho\varphi_{\mathrm g}$ in the
   total energy was "crucial" at low Mach.
9. **Ranking** (§6). α-β and deviation are far better than Cargo–LeRoux;
   deviation is preferred for generality.

**Tests** (§5, 2D unless stated):
* **Isothermal, isentropic and polytropic atmospheres**, run to 5000
  buoyancy times. Without balancing, the 1D isothermal case reaches
  Mach $10^{-6}$–$10^{-5}$; with any balancing it stays below $10^{-12}$.
* **Rising hot bubble** with an amplitude scan from $10^{-3}$ to
  $10^{-11}$. α-β and deviation follow
  $\mathrm{Ma} \propto (\Delta A/A)^{1/2}$ down to Mach about $10^{-6}$.
* **Heated convection** reaching $\mathrm{Ma}_{\mathrm{rms}} \approx 2.1\times10^{-4}$.
* **Keplerian disk** for up to $10^4$ orbits, with the deviation method only.
* **Shell convection on a cubed sphere** (§6).

# Notation map

| Edelmann et al. (2021) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\varrho$, $\mathbf v$, $p$, $E$ | $\rho$, $\mathbf v$, $p$, $E$ | $E$ includes $\rho\varphi_{\mathrm g}$ here |
| $\phi$, $\mathbf g$ | $\varphi_{\mathrm g}$, $\mathbf g$ | $\phi_i$ is the PPM flattening |
| $\mathbf s$, $\hat S$ | $\mathbf s(u)$ | registry $s$ is the stage count |
| $\tilde{\mathbf u}$; $\Delta\mathbf u$ | $u^{\mathrm{eq}}$; $u - u^{\mathrm{eq}}$ | |
| $\alpha(x)$, $\beta(x)$ | hydrostatic profiles (words) | collide with $\alpha$, $\beta_k$ |
| $q$, $\Pi$ (Cargo–LeRoux) | words | collide with $q$, $\Pi$ |
| $M$, Ma, $M_{\mathrm{cut}}$, $f_a$ | $\mathrm{Ma}$, $\mathrm{Ma}_{\mathrm{cut}}$, $\mu_{\mathrm{pc}}(2 - \mu_{\mathrm{pc}})$ | |
| $c_{\mathrm{CFL}}$; $\nu$ (polytropic index) | $\nu$; words | |
| $\boldsymbol\xi$, $J$ | $\mathbf X$, $\mathcal J$ | |

# Pages created or updated

* Created [Well-balanced schemes](/properties/well-balanced.md), [Low-Mach-number numerical fluxes](/methods/low-mach-number-fluxes.md).
* Updated [Approximate Riemann solvers](/methods/approximate-riemann-solvers.md) (low Mach).
* Updated [Notation registry](/notation.md): $\mathbf s(u)$, $u^{\mathrm{eq}}$, $\varphi_{\mathrm g}$, $\mathbf g$, $\mathrm{Ma}$.

# Citations

1. `~/papers/mosaic/high-order-capturing-schemes/2021-A&A-Edelmann-10105100046361202140653.pdf`.
   * **Version.** arXiv:2102.13111v2 (8 July 2021), the accepted
     manuscript in A&A proof layout, 26 pages including Appendices A–D.
     It is not the typeset article.
   * **Identity.** doi:10.1051/0004-6361/202140653, checked on Crossref:
     Astron. Astrophys. 652:A53, August 2021, with the same eight authors.
   * **How it was read.** Text extraction, all sections. Eqs. 29–72 were
     checked on the page images.
   * **A labelling slip.** The §5 preamble labels the cut-off Mach numbers
     as "$f_a$" values.
   * **Reference list:** 83 entries. A&A style prints no article titles.
