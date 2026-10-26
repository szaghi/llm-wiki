---
type: Source
title: "Cernetic et al. (2024) — Supersonic turbulence simulations with GPU-based high-order Discontinuous Galerkin hydrodynamics"
description: "Makes a GPU modal discontinuous Galerkin code robust for driven isothermal turbulence up to Mach 12.8 with a von Neumann–Richtmyer viscous pressure at internal quadrature points and a projection of primitive variables, and finds DG's resolution advantage over second-order finite volume nearly lost in supersonic turbulence."
resource: "doi:10.1093/mnras/stae2192"
source_kind: paper
authors: [Cernetic M., Springel V., Guillet T., Pakmor R.]
year: 2024
venue: "Mon. Not. R. Astron. Soc. 534:1963–1984"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Monthly_Notices_of_the_Royal_Astronomical_Society_Cernetic_Supersonic_turbulence_simulations_with_GPU-based_high-order.pdf"
tags: [dg, compressible, astrophysics, numerical-dissipation, implicit-les, gpu]
timestamp: 2026-10-26T15:48:00Z
---

# Summary

Cernetic et al. (2024) test whether their GPU-accelerated, MPI-parallel
discontinuous Galerkin code keeps its accuracy advantage over a second-order
finite-volume scheme in driven, isothermal, supersonic turbulence, where the
flow is a network of interacting shocks. The DG is **modal**: Legendre
polynomials on Cartesian cells, truncated to total degree $N$, with an HLLC
interface flux and SSP Runge–Kutta time stepping. It is not the nodal
collocation [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md).
Two changes make high Mach numbers stable.

- **Artificial viscosity.** The authors' earlier evolved-viscosity field with
  shock and "wiggle" sensors is replaced by a classical von Neumann–Richtmyer
  viscous pressure, quadratic (and optionally linear) in the compression rate.
  It is added only at the internal Gauss points and capped
  ([artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)).
  This is an alternative to
  [subcell finite-volume shock capturing](/methods/subcell-finite-volume-shock-capturing.md).
- **Projection of primitive variables.** The primitive variables are
  re-projected onto the basis from their values at the internal Gauss points
  before being extrapolated to the faces. The face velocity is no longer the
  ratio of the momentum and density polynomials, which can take extreme
  values.

Shu–Osher and Liska–Wendroff tests show sub-cell shock capture up to order 10
and less diffusion than finite volume. In a $256^3$ suite of solenoidally
driven [isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md)
at rms Mach 0.1–12.8, DG markedly extends the resolved spectral range in the
subsonic regime. This advantage "nearly disappears" in the supersonic regime,
and all schemes reproduce the transition from $k^{-5/3}$ to $k^{-2}$. The
turbulence runs use no subgrid model and the paper states no physical
viscosity for them, so they are [implicit LES](/definitions/implicit-les.md),
dissipated by the
scheme's [numerical dissipation](/properties/numerical-dissipation.md) and the
artificial viscosity, and DG shows a pronounced
[bottleneck](/definitions/bottleneck-effect.md). At $1024^3$ and Mach 3.2,
second-order DG resolves the sonic scale, where the structure-function slope
changes from about $0.5$ to $0.4$. Finite volume at $1024^3$ smears it, and DG
at $512^3$ does "nearly as well as" finite volume at $1024^3$. An
operation-count model gives a cost of $\propto N_x^4N^8$ to a fixed end time.
With idealized error models, high order pays for smooth flows but not for a
single planar shock. For shock-dominated problems the authors expect the best
choice to be order 2 or 3. The flows are shock networks formed by
astrophysical compressible turbulence, the converse process treated in the
last section of [shock-generated turbulence](/results/shock-generated-turbulence.md),
not shock-driven mixing; the paper does not use [WENO](/methods/weno-scheme.md).

# Version read

arXiv 2401.06841v2 (1 October 2024), the accepted manuscript in MNRAS LaTeX
("Accepted 2024 September 11"), 22 pages, all read (pp. 3, 4, 5, 8, 12, 19,
20 checked visually). Page numbers are the preprint's 1–22, not the journal's
1963–1984; the running header "MNRAS 000, 1–22 (2023)" is a template
placeholder. Title and authors match Crossref.

# Key claims

1. A von Neumann–Richtmyer viscous pressure $p_{\mathrm{av}}$ added at internal Gauss points only, with the Riemann solver supplying the entropy at faces, captures shocks at sub-cell resolution in DG at every tested order, with no storage overhead (§3.1, Eqs. 14–16; Conclusions). **Shown**
2. Recommended $\alpha_{\mathrm{visc}}\sim2.0$ and $\beta_{\mathrm{visc}}\sim0.2$ give "a good compromise between stability, narrowness of shocks, and the damping of postshock oscillations, largely independent of flow type and DG-order"; typical range $\alpha_{\mathrm{visc}}\simeq1.0$–$3.0$, $\beta_{\mathrm{visc}}=0$ or $\simeq0.1\,\alpha_{\mathrm{visc}}$ (§3.1). **Stated** (empirical)
3. The value of $\alpha_{\mathrm{visc}}$ does not set the post-shock state, since the total dissipation at a shock is fixed by the conservation laws; it only affects shock sharpness and residual oscillations (§3.1). **Stated**
4. DG on the Euler equations has no sub-cell entropy source: unlike finite volume it lacks the entropy produced by the cell averaging at the end of every step, an advantage for advection but an impediment at shocks (§3.1). **Stated**
5. Face velocities computed as the ratio of momentum and density polynomials can take "extreme" values in strongly shocked turbulence ($32^3$ cells, "expansion order $p=3$" as printed, Mach $\simeq3$ skewer, Fig. 3); projecting the primitive variables "drastically improves the robustness and the quality of results" for supersonic turbulence and strong shocks, with no tangible difference for smooth problems (§3.2, Eq. 17). **Shown**
6. The two changes together allow stable driven isothermal turbulence at Mach 12.8 with high-order DG, which "has previously been met with severe stability problems" (Conclusions). **Shown**
7. Shu–Osher at $t=1.8$: order-2 DG beats second-order finite volume at 100, 200 and 400 cells, especially for the short waves; orders 4 (100 cells), 5 or 6 (200 cells, see Printed slips) and 10 (400 cells) are stable, and order 10 shows no ringing (§3.1.1, Fig. 1). **Shown**
8. Liska–Wendroff implosion at $t=2.5$ on $400^2$ cells: order-2 DG keeps the symmetry, shows "clearly less numerical diffusion" than finite volume, and, in the authors' words, "appears close to or even better than" the third-order PPM result of ATHENA (§3.1.2, Fig. 2). **Shown** (qualitative comparison)
9. At $256^3$, DG of order 2 and more so order 3 extend the resolved range of the velocity spectrum over second-order finite volume in the subsonic regime; order 3 shows a more pronounced bottleneck (§5, Fig. 5). **Shown**
10. In the supersonic regime the gain of DG over finite volume "nearly disappears"; DG accuracy is "at least comparable or even slightly better" (§5, Fig. 5). **Shown**
11. All schemes reproduce the transition from $E(k)\propto k^{-5/3}$ (subsonic) to $E(k)\propto k^{-2}$ (supersonic) (§5, Fig. 5). **Shown**
12. Structure-function slopes fitted over $0.1<l<0.25$ at $256^3$, order-2 DG: 0.32 in the most subsonic and 0.47 in the most supersonic run, against the expected $1/3$ and $1/2$ (Fig. 6). **Shown**
13. Density PDFs at $256^3$ are close to log-normal, widen strongly with Mach number and are nearly identical for the three schemes; at $1024^3$, Mach 3.2, DG resolves slightly larger density contrasts than finite volume "despite our use of artificial viscosity" (§5, Fig. 7). **Shown**
14. The Mach 12.8 finite-volume and order-3 DG runs show excess scatter at low densities from the density floor $10^{-3}$, absent in order-2 DG (Fig. 7 caption). **Shown**
15. At $1024^3$, Mach 3.2, order-2 DG: a settling region from $L/2$ to $\sim L/6$, then $v(l)\propto l^{0.5}$ (fit 0.49) up to a sudden change to $\propto l^{0.4}$ (fit 0.43), identified as the sonic point; the scale where $v(l_s)=c_s$ lies close to but not at the kink (§6, Fig. 8). **Shown**
16. The $1024^3$ DG velocity spectrum follows $k^{-2}$ just beyond the driving range and then flattens toward $k^{-5/3}$; the intersection of the two power laws lies "reasonably close" to the sonic scale from the structure function; a prominent bottleneck is present (§6, Fig. 10). **Shown**
17. Order-2 DG at $512^3$ "does nearly as well as" finite volume at $1024^3$ in resolving the sonic point; finite volume at $512^3$ shows no trace of it, and at $1024^3$ has a flatter-than-expected supersonic slope and an earlier transition to dissipation (§6, Fig. 11). **Shown**
18. The expected sonic wavenumber is $k_s\simeq k_{\mathrm{inj}}M_t^2$ ($l_s=L_{\mathrm{inj}}/M_t^2$), so at $M_t=3.2$ the sonic point is "only about a factor of 10 away from the injection scale" (§4.1, Eq. 22; §6). **Derived** (from $v(l)\propto l^{1/2}$)
19. Following Pan et al. (2022), the density-weighted Mach number scales as $M_t^{0.96}$ in the supersonic regime, "which matches our own findings very closely" (§4.1). **Stated** (no data shown)
20. The turbulence is fully developed only for $t\ge2T$; dissipation starts after about one eddy turnover and quasi-stationarity is reached by $t\simeq3T$; statistics are averaged over $3T<t<8T$ (§4.2, Fig. 9). **Shown**
21. With a fixed driving recipe the realized Mach numbers match the intended doubling in the subsonic regime and "fall slightly short" well above unity (§5). **Shown** (not tabulated)
22. One evaluation of the right-hand side costs $C_{\dot w}=\tfrac53N_x^3(N+1)^2(5N^4+50N^3+175N^2+259N+183)$ operations, i.e. $\propto N^6$ per cell (§7, Eq. 33). **Derived** (operation count)
23. The total cost to a fixed end time is $C_{\mathrm{tot}}\propto N_x^4N^8$ in three dimensions (§7, Eq. 35). **Derived**
24. For a smooth problem with $L_1=a_NN_x^{-(N+1)}$, high order is cheapest for large problems and small target errors; for a single planar shock with $L_1=b\,N_x^{-1}(N+1)^{-1}$ it is "always computationally favorable" to raise $N_x$ rather than $N$ (§7, Figs. 13–14). **Derived** (model, no timings)
25. With many shocks present, DG above order 3 is unlikely to be cost-effective; the sweet spot is expected at order 2 or 3 (Conclusions). **Stated** (from the cost model and the turbulence runs)
26. Suggested remedy: $h$-refinement at shocks and $p$-refinement in smooth regions (§7). **Stated**

The viscous pressure (Eqs. 14–16), with $h$ the cell size and $h/(N+1)$ the
effective resolution, applied only where $\nabla\cdot\boldsymbol u<0$:

$$p_{\mathrm{av}}=\alpha_{\mathrm{visc}}\,\rho\Big(\frac{h}{N+1}\Big)^2\lvert\nabla\cdot\boldsymbol u\rvert^2\;\Big[+\;\beta_{\mathrm{visc}}\,\rho c_s\frac{h}{N+1}\lvert\nabla\cdot\boldsymbol u\rvert\Big],\qquad p_{\mathrm{av}}\le\frac12\rho\Big(\frac{h}{N+1}\Big)^2\frac{\lvert\nabla\cdot\boldsymbol u\rvert}{\Delta t}.$$

The paper prints the two forms separately and says the linear one "augments"
the quadratic one.

# Printed slips

- **Eq. 35:** printed $\tfrac56N_x^4(1+N)^4(10N^4+100N^3+315N^2+523N+372)$. Expanding the printed ingredients ($(N+1)^3$ volume and $(N+1)^2$ face points, $\tfrac16(N+1)(N+2)(N+3)$ coefficients per field, 5 fields, 15 operations per flux, Eq. 33 and the first line of Eq. 35) gives $351N^2$, not $315N^2$; the same ingredients reproduce Eq. 33 exactly *(compiler check, not in the sources)*. The leading scaling is unaffected.
- **Eq. 13:** $dA/dt=-\tfrac12\frac{\gamma-1}{\rho^\gamma}p_{\mathrm{av}}\nabla\cdot\boldsymbol u$ for $A=p/\rho^\gamma$. With $p=(\gamma-1)\rho e_{\mathrm{int}}$, $d\rho/dt=-\rho\nabla\cdot\boldsymbol u$ and the viscous pressure working in the internal-energy equation as $\rho\,de_{\mathrm{int}}/dt=-(p+p_{\mathrm{av}})\nabla\cdot\boldsymbol u$ ($e_{\mathrm{int}}$ the specific internal energy, the source's $u$), the continuum equation is $dA/dt=-\frac{\gamma-1}{\rho^\gamma}p_{\mathrm{av}}\nabla\cdot\boldsymbol u$, without the $\tfrac12$ *(compiler check, not in the sources)*. The paper does not derive Eq. 13, so whether the $\tfrac12$ reflects another convention is not settled by the text.
- **Eq. 8:** orthonormality printed with $\delta_{l,k}$ for $\delta_{l,m}$.
- **Eqs. 2 and 4:** $e$ is defined as the total energy per unit volume, $\rho u+\tfrac12\rho\boldsymbol v^2$, but the energy flux is printed $(\rho e+p)v_x$.
- **§4.2:** "For doubling the Mach number, we thus need to triple our driving strength $E_{\mathrm{inj}}$", while Eq. 32 gives $M\propto E_{\mathrm{inj}}^{1/3}$, so doubling needs a factor $2^3=8$ *(compiler check, not in the sources)*.
- **§4.1:** density-weighted Mach number printed $\langle\rho\boldsymbol v^2/(\bar\rho c_s)\rangle^{1/2}$, with $c_s$ not squared; the equivalent form $(2E_{\mathrm{kin}}/M_{\mathrm{tot}})^{1/2}/c_s$ printed next to it is consistent.
- **Eq. 10 context:** "$L_1\propto h^{-(k+1)}$" with $h$ the cell size; elsewhere $L_1\propto N^{-(k+1)}$ with $N$ cells.
- **§3.1.1:** Shu–Osher state "for $z<-4$" (should be $x$); the text says "ringing at $N_{\rm cell}=200$ with $p=6$" while the Fig. 1 panel is labelled "DG-5-N200".
- **Fig. 2 caption:** DG "(right panel)" and finite volume "(left panel)", while the panels are labelled DG-2 on the left and FV-2 on the right.
- **§5:** "DG simulations of order $k=2$" (the caption says $p=2$); "the $1024^3$ runs of DG-1 and FV" (the figure and Table 1 show DG-2).
- **Table 1** lists only DG for the $256^3$ Mach sweep, while Figs. 5 and 7 include matching finite-volume runs.
- **Fig. 6 caption:** "average of 96 power spectra measurements" for a structure-function figure; **Fig. 11 caption:** "the supersonic and supersonic regimes".
- **§4.3:** minimum separation $L/[pN]$ explained with "$k$ the maximum polynomial order".
- **§4.2:** "$\sigma$ is the variance", while $\sigma$ enters as an amplitude ($\sigma^2$ in Eq. 28).
- Typos: "Implostion test" (§3.1.2 heading), "manifest conversation of mass" (§2.3), "with and adiabatic index".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\boldsymbol v$ | $\boldsymbol u$ (velocity) | |
| $\boldsymbol u=(\rho,\rho\boldsymbol v,e)$ | (conserved state vector) | **collision:** bold $\boldsymbol u$ is not the velocity |
| $u$ | (specific internal energy) | **collision** with the velocity |
| $e$ | $E$ (total energy per unit volume) | |
| $k$ | $N$ (polynomial degree) | **collision:** $k$ is also the wavenumber |
| $p=k+1$ | $N+1$ (order) | **collision:** $p$ is also the pressure |
| $N$ (Eq. 5) | (number of basis functions per cell) | **collision** with the degree $N$ |
| $N$ (cells per dimension), $N_{\mathrm{cell}}$ | $N_x$ | |
| $\phi_l^K$, $\boldsymbol w_l^K$ | (modal Legendre basis, total degree $\le N$; modal weights) | modal, not nodal DGSEM |
| $h$ | $h$ (cell size) | |
| $\Pi$ | $p_{\mathrm{av}}$ (von Neumann–Richtmyer viscous pressure, page-local, as on the [artificial-viscosity page](/methods/artificial-viscosity-shock-capturing.md)) | **collision** with the SGS energy flux $\Pi$ |
| $\alpha_{\mathrm{visc}}$, $\beta_{\mathrm{visc}}$, $\Pi_{\max}$ | $C_{\mathrm q}$, $C_{\mathrm l}$ (quadratic and linear viscosity coefficients, page-local on the artificial-viscosity page), (cap) | kept as printed in the key claims; **collision:** $\alpha$ is not the DG/FV blending factor |
| $A=p/\rho^\gamma$ | $A_s$ (entropic function, page-local on the artificial-viscosity page) | |
| $\varepsilon$ (Eq. 11) | (diffusion coefficient) | **collision** with the dissipation rate |
| $\epsilon$ | $\varepsilon$ (energy injection rate per unit mass; equal to the dissipation rate in the stationary state) | |
| $\mathcal M=\langle\boldsymbol v^2/c_s^2\rangle^{1/2}$ | $M_t$ (rms Mach number) | volume-weighted |
| $\mathcal M_\rho$ | (density-weighted rms Mach number) | |
| $c_s$ | (isothermal sound speed; $c$ on the artificial-viscosity page) | |
| $v(l)$, $\mathcal M(l)$ | (characteristic velocity from the second-order structure function, scale-dependent Mach number) | |
| $l_s$, $k_s$ | (sonic scale, sonic wavenumber; page-local) | $v(l_s)=c_s$ |
| $L$, $L_{\mathrm{inj}}$, $k_{\mathrm{inj}}$ | (box size, injection scale $L/2$, injection wavenumber) | **collision:** $L$ is not the integral length scale |
| $E_v(\boldsymbol k)$, $E(k)=4\pi k^2\langle E_v\rangle$ | $E(k)$ | built from $\lvert\boldsymbol u_{\boldsymbol k}\rvert^2$ without the factor $\tfrac12$ |
| $T=L/(2c_s\mathcal M)$ | (large-eddy turnover time) | |
| $t_c$, $\sigma$, $f$, $E_{\mathrm{inj}}$ | (Ornstein–Uhlenbeck correlation time, amplitude, decay factor, driving strength) | **collision:** $f$ also counts the conserved fields (§7) and is not the body force $f_i$ |
| $b_k$ | (coefficients per field; prefactor of the shock error model) | overloaded in §7 |
| DG-$n$, FV-2 | order-$n$ DG ($N=n-1$), second-order finite volume | |

# Reference list

64 printed references, MNRAS author–year style without article titles. The
list is merged complete into the [bibliography](/bibliography.md) with
`citedby` this slug. The two Cockburn et al. 1989 works take suffixes in
printed order. Reed & Hill (1973) prints no venue, Frisch (1995) no
publisher, and Tassis et al. (2018) is an arXiv preprint. The companion paper
Cernetic et al. (2023, MNRAS 522) is a distinct entry. No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-26). This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Bottleneck effect in the energy spectrum](/definitions/bottleneck-effect.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
