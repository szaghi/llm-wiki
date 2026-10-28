---
type: Source
title: "Chapelier et al. (2024) — Comparison of high-order numerical methodologies for the simulation of the supersonic Taylor–Green vortex flow"
description: "Seven-code comparison on the supersonic Taylor–Green vortex (Re=1600, M=1.25) against a 2048³ sixth-order TENO reference: kinetic energy, solenoidal and dilatational dissipation and Mach profiles rank artificial diffusivity, scheme switching, TENO and filtering as shock-capturing families in implicit LES."
resource: "doi:10.1063/5.0206359"
source_kind: paper
authors: [Chapelier J.B., Lusher D.J., Van Noordt W., Wenzel C., Gibis T., Mossier P., Beck A., Lodato G., Brehm C., Ruggeri M., Scalo C., Sandham N.]
year: 2024
venue: "Phys. Fluids 36:055146"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2024_Crossref_Physics_of_Fluids_Chapelier_Comparison_of_high-order_numerical_methodologies_for_the_sim.pdf"
tags: [compressible, implicit-les, numerical-dissipation, dg, high-order, dns]
timestamp: 2026-10-28T07:10:00Z
---

# Summary

Chapelier et al. (2024) compare seven solvers on the supersonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) of Lusher & Sandham
(2021), at $Re=1600$ and $M_0=1.25$. The case combines transition, decaying
turbulence, strong shocks and shock–turbulence interaction, and starts from an
analytic initial condition that any solver can reproduce. The authors present
it as the first cross-comparison of methodologies on this case. The solvers
and their shock capturing are:

- CODA: modal DG, order 4, localized artificial diffusivity with a
  Persson–Peraire sensor weighted by the Ducros function;
- SPADE: eighth-order central kinetic-energy- and entropy-preserving finite
  differences ([kinetic-energy preservation](/properties/kinetic-energy-preservation.md)),
  blended with a third-order WENO flux through the Ducros sensor;
- OpenSBLI: sixth-order TENO finite differences
  ([WENO and TENO](/methods/weno-scheme.md));
- NS3D: sixth-order compact finite differences with a tenth-order compact
  filter and no shock capturing;
- SD3DvisP: fourth-order [spectral difference](/methods/spectral-difference-method.md) with artificial diffusivity
  ([artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md));
- [FLEXI](/software/flexi.md): fourth-order
  [DGSEM](/methods/discontinuous-galerkin-spectral-element-method.md) with a
  [second-order finite-volume subcell](/methods/subcell-finite-volume-shock-capturing.md)
  shock capturing;
- H3AMR: [flux reconstruction](/methods/flux-reconstruction.md) at second
  order, with the "Block Spectral Stresses" model.

No solver uses a subgrid model. The coarse runs are treated as
[implicit LES](/definitions/implicit-les.md), on the assumption that the
schemes' inherent dissipation mimics the subgrid dissipation at this low
Reynolds number. The $512^3$ runs are expected to resolve the turbulence
nearly as a [DNS](/definitions/direct-numerical-simulation.md) does. The
reference is a $2048^3$ OpenSBLI TENO run, which cost 1.96 million core hours.

The kinetic energy is captured by every solver from $128^3$ degrees of
freedom. At $64^3$ the
[numerical dissipation](/properties/numerical-dissipation.md) of the
Riemann-flux codes lowers the early energy, the dissipation-free central
codes pile up energy late, and the second-order code over-dissipates. The
dilatational dissipation ranks shock-capturing strength, and its first peak
is not mesh-converged even at $2048^3$. The solenoidal dissipation is mostly
captured from $256^3$, and is highest for CODA, FLEXI and NS3D. Artificial
diffusivity gives thick, oscillation-free shocks. Switching to a lower-order
scheme gives sharp but oscillating shocks on coarse grids, except TENO, which
stays sharp and oscillation-free. Compressible isotropic turbulence with
shocklets ([isotropic turbulence](/benchmarks/homogeneous-isotropic-turbulence.md))
is named as the closest physical flow. Shocks interacting with wall turbulence
([shock–boundary-layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md))
are named as future work. The flow is shock–turbulence interaction in a
periodic box, which [shock-generated turbulence](/results/shock-generated-turbulence.md)
lists among the flows where turbulence forms its own shocks, not among the
shock-driven mixing problems.

# Version read

HAL deposit hal-04582857v1 (22 May 2024) of the authors' accepted manuscript
(AIP "ACCEPTED MANUSCRIPT" stamp on every page), 39 PDF pages: a HAL cover
page and 38 manuscript pages, of which pp. 33–38 are the references. All
pages were read, and pp. 4–9 were checked visually. Page and figure numbers
are those of the manuscript (manuscript p. 1 = PDF p. 2). Title and the 12
authors match Crossref.

# Key claims

1. The supersonic Taylor–Green vortex is used for the first time (to the authors' knowledge) in a cross-comparison of numerical methodologies; it features transition, developed turbulence, strong shocks and shock–turbulence interaction from an analytic initial condition (§I, p. 3). **Stated**
2. The closest physical flow is compressible isotropic turbulence with shocklets, which "might resemble the later stages" of the supersonic case (§I, p. 3). **Stated**
3. With sixth-order TENO the kinetic energy $E_k$ converges fast: $128^3$ captures the large-scale energy (resolutions $64^3$ to $2048^3$) (§II.C, Fig. 2). **Shown**
4. The solenoidal dissipation $\varepsilon_s$ needs $512^3$ with sixth-order TENO "for converging towards the exact values and capture all turbulent scales" (§II.C, Fig. 3). **Shown**
5. The dilatational dissipation $\varepsilon_d$ has two peaks, the first from shocks with little vortex interaction, the second from the onset of shock–turbulence interaction; the first is **not mesh-converged even at $2048^3$**, because shocks keep sharpening until molecular viscosity smooths them; the second converges faster (§II.C, Fig. 4). **Shown**
6. The $2048^3$ reference used 57 600 A64FX cores (1200 nodes), 4800 MPI ranks × 12 OpenMP threads, $\Delta t=2.5\times10^{-4}$, 80 000 steps to $t=20$ at about 1.53 s per step: 34 h, 40 800 node hours, 1.96 million core hours; one snapshot is 520 GB in double precision (§II.C, p. 7). **Shown** (reported run data)
7. All shock-capturing approaches except NS3D act only where a sensor fires, so the nominal order holds away from shocks; NS3D's filter is of higher order than the scheme, so the nominal order holds there too (§III.A, p. 12). **Stated**
8. At $64^3$ CODA (DG), SD3DvisP and OpenSBLI under-predict the early $E_k$, attributed to the dissipation of their Riemann-based interface fluxes (§IV.A, Fig. 5). **Shown** (attribution **Stated**)
9. At $64^3$ the central finite-difference codes SPADE and NS3D predict $E_k$ very accurately up to $t\approx12$ and slightly too high afterwards, explained by a small-scale pile-up near the cutoff and the lack of a subgrid closure (§IV.A, Fig. 5). **Shown** (explanation **Stated**)
10. FLEXI's $E_k$ is closer to the finite-difference codes than to CODA and SD3D although it uses the same kind of Riemann flux; the difference is attributed to its finite-volume subcell shock capturing in place of artificial diffusivity (§IV.A). **Shown** (attribution **Stated**)
11. The second-order H3AMR under-predicts $E_k$ at $64^3$, the excess dissipation typical of second-order upwind schemes; higher-order schemes with the same degrees of freedom do better (§IV.A, Fig. 5). **Shown**
12. Low $\varepsilon_d$ indicates strong shock capturing with smooth thick shocks; high $\varepsilon_d$ indicates sharp shocks at risk of oscillation, which show up as oscillations of $\varepsilon_d(t)$ (§IV.A, p. 22; §V). **Stated** / **Shown**
13. NS3D gives the highest $\varepsilon_d$, oscillating around the first peak at all resolutions; FLEXI is slightly lower with comparable oscillations on the coarser grids (DG/finite-volume switching per element); CODA and OpenSBLI are lower and less oscillatory, OpenSBLI oscillation-free at all resolutions, CODA slightly oscillating from $256^3$; SPADE, SD3D and H3AMR give the lowest $\varepsilon_d$ on all grids (§IV.A, Fig. 6). **Shown**
14. CODA, FLEXI and NS3D give the highest $\varepsilon_s$ on all grids (lenient shock capturing that leaves the small scales alone); SPADE is lower; SD3D is high on the coarse grid and lower on finer ones; OpenSBLI is low on coarse grids but converges well; H3AMR is lowest on all grids (§IV.A, Fig. 7). **Shown**
15. Most of the turbulent dynamics is captured by every solver from $256^3$; on coarser grids high-order schemes still capture much of the small-scale dynamics, and discontinuous finite-element schemes "seem to be efficient in that respect" (§IV.A, p. 23). **Shown**
16. Mach-number profiles at $t=2.5$ along the $y$ line at $x=z=0$: on $64^3$ and $128^3$ NS3D has the strongest Gibbs oscillations; SD3D thick oscillation-free shocks; TENO sharp and oscillation-free in all cases; CODA sharp with limited oscillations; FLEXI the sharpest shocks, matching the reference at $256^3$ but oscillating below (§IV.B, Fig. 8). **Shown**
17. Several shock-capturing techniques oscillate on coarse grids and the oscillations vanish under refinement; TENO and the artificial-diffusivity schemes mitigate them best at all resolutions; a technique consistent across resolutions is hard to obtain (§IV.B, p. 27). **Shown**
18. Artificial diffusion yields smooth but thick shocks on coarse grids; local switching to lower-order schemes yields sharp but oscillating shocks, except TENO; the filter-only finite-difference scheme gives the largest oscillations (§V, p. 29). **Shown**
19. DG, spectral difference and DGSEM capture small scales well on coarse grids, as does high-order finite differences with high-order filtering; finite differences with local scheme switching and high-order TENO "yield more small-scale dissipation"; high order beats second order for both large and small scales here (§V, p. 29). **Shown**
20. Overall, shock capturing has "a low impact … on the representation of turbulent scales" (§V, p. 29). **Shown** (the authors' synthesis)
21. In NS3D post-processing, explicit fourth-order derivatives in place of the sixth-order compact scheme change $\varepsilon_s$ by up to 5 % in the supersonic case (§III.B.d, p. 16). **Shown** (reported, no figure)
22. Verification at $Re=500$, $M_0=0.5$: all codes agree on $E_k$ and $\varepsilon_s$ up to $t=10$ and on $\varepsilon_d$ up to $t=9$, with minor later discrepancies attributed to short acoustic waves (App. A, Figs. 9–10). **Shown**
23. A case at $Re=500$, $M_0=0.1$ was fully resolved in $E_k$ and enstrophy by a Fourier spectral method at $128^3$ (App. A, p. 31, cited). **Stated**
24. TENO improves on ENO/WENO with considerably lower numerical dissipation and robust shock capturing, through an ENO-like staggered stencil layout and a strong scale-separation procedure (§II.C, pp. 6–7, cited). **Stated**
25. Time integration is not assessed: all solvers use classical third- or fourth-order Runge–Kutta schemes (§III.A, p. 12). **Stated**

The diagnostics (Eqs. 9–11), with $\mathcal V$ the domain and $\mu_0$ the
reference viscosity:

$$E_k=\frac{1}{2\rho_0V_0^2\lvert\mathcal V\rvert}\int_{\mathcal V}\rho\,\boldsymbol u\cdot\boldsymbol u\,dV,\qquad
\varepsilon_s=\frac{L^2}{Re\,V_0^2\lvert\mathcal V\rvert}\int_{\mathcal V}\frac{\mu}{\mu_0}\,\omega_i\omega_i\,dV,\qquad
\varepsilon_d=\frac{4L^2}{3Re\,V_0^2\lvert\mathcal V\rvert}\int_{\mathcal V}\frac{\mu}{\mu_0}(\nabla\cdot\boldsymbol u)^2\,dV.$$

# Printed slips

- **Eq. 5:** $p=(\gamma-1)\big(\rho E-\tfrac12\mathbf u\cdot\mathbf u\big)$; with $\rho E$ the total energy per unit volume, the kinetic term needs $\rho$ *(compiler check, not in the sources)*.
- **§II.B, p. 5:** $Re=\rho_0U_0/\mu_0$ is printed without the length $L$ *(compiler check, not in the sources)*.
- **SD3D operator:** §III.B.e says the artificial diffusion "acts as a bulk viscosity on the momentum equations, and as a thermal diffusivity on the energy equation. No artificial diffusion is considered for the mass conservation equation"; §III.B.h says "For SD3D and CODA, it takes the form of a Laplacian operator impacting all conservative variables".
- **Fig. 8:** the legend prints "Ref. TENO6 512", while the text and Figs. 5–7 give the reference as the $2048^3$ TENO run; the bottom-right panel is labelled "y" instead of "y/L".
- **App. A:** the text gives the verification resolutions without FLEXI, while the Fig. 9 legend lists "FLEXI 384".
- **"262.000 CPUs"** (p. 17) for 262 000.
- **Reference list:** the same co-author is printed "J. L. Hill" (refs. 22, 61) and "J. J. Hill" (ref. 62); ref. 62 has no title.
- Typos: "allowing as assessment" (p. 3), "single- und multiphase" (p. 18), "accross" (p. 27), "stabilazation" (p. 29), "occurence" (p. 17), "mimicks" (p. 19).

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\rho$, $\mathbf u$, $p$, $T$ | $\rho$, $\boldsymbol u$, $p$, $T$ | |
| $E$ (per unit mass), $\rho E$ | $E/\rho$, $E$ | **collision:** the registry's $E$ is per unit volume |
| $\boldsymbol\tau$ | $\sigma_{ij}$ (viscous stress) | **collision** with the SGS stress $\tau_{ij}$ |
| $\lambda=\mu C_p/Pr$ | (thermal conductivity) | **collision** with the Taylor microscale |
| $C_p$, $Pr=0.71$, $\gamma=1.4$ | $c_p$, $Pr$, $\gamma$ | |
| $U_0$ | $V_0$ (reference velocity, as on the Taylor–Green page) | |
| $M_0=U_0\sqrt{\rho_0/(\gamma p_0)}$ | $M_0$ (reference Mach number) | |
| $\Omega$, $\lvert\Omega\rvert$ | $\mathcal V$, $\lvert\mathcal V\rvert$ (domain, page-local) | **collision** with the rotation-rate tensor |
| $\boldsymbol\omega$ | $\omega_i$ (vorticity) | |
| $E_k$ | (normalized volume-averaged kinetic energy) | $\rho$-weighted |
| $\epsilon_s$, $\epsilon_d$ | $\varepsilon_s$, $\varepsilon_d$ (solenoidal and dilatational dissipation, registry §11) | |
| $N$ | $N_x^3$ (total degrees of freedom, §II.C); $N$ (DGSEM degree, FLEXI); $N+1$ (H3AMR points per direction = order) | three meanings in the source |
| $p$ (CODA) | $N$ (polynomial degree; order 4 = $N=3$) | **collision** with the pressure |
| $C_T=10^{-6}$ | $C_T$ (TENO cut-off threshold, registry §11) | |
| $C_\varepsilon=0.5$ | (SD3D artificial-viscosity amplitude) | |
| $\alpha=0.4$ | (NS3D compact-filter parameter) | **collision** with the DG/FV blending factor |
| DoFs | (degrees of freedom: grid points for finite differences, elements × modes or nodes for element methods) | |
| LAD | localized artificial diffusivity | |

# Reference list

63 printed references, AIP numbered style. The list is merged complete into
the [bibliography](/bibliography.md) with `citedby` this slug. Same-author
same-year pairs (Lusher & Sandham 2021, Bassi & Rebay 1997, Bemis et al. 2023)
take suffixes in printed order. Ref. 55 (Blind et al., arXiv:2306.12891, FLEXI
exascale) is a preprint distinct from the ingested
[Blind et al. (2023)](/sources/blind-2023.md) and is re-keyed `blind-2023-b`; ref. 21 is
[Krais et al. (2021)](/sources/krais-2021.md). Refs. 52 and 54 are bare GitHub
URLs, ref. 35 prints no proceedings title, ref. 62 no title, and ref. 63 is an
arXiv preprint without identifier. No printed duplicates.

# Pages created or updated

Chunk 6 (2026-10-26), cited further in chunks 7, 8, 14. This source is cited on:

- [Homogeneous isotropic turbulence (decaying and forced)](/benchmarks/homogeneous-isotropic-turbulence.md)
- [Shock–turbulent boundary layer interaction](/benchmarks/shock-turbulent-boundary-layer-interaction.md)
- [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
- [Bulk viscosity](/definitions/bulk-viscosity.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Implicit large-eddy simulation](/definitions/implicit-les.md)
- [Shock sensors and troubled-cell indicators](/definitions/shock-sensor.md)
- [Artificial-viscosity shock capturing](/methods/artificial-viscosity-shock-capturing.md)
- [Compact finite-difference schemes](/methods/compact-finite-difference-scheme.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Flux reconstruction](/methods/flux-reconstruction.md)
- [Spectral difference method](/methods/spectral-difference-method.md)
- [Subcell finite-volume shock capturing for DG](/methods/subcell-finite-volume-shock-capturing.md)
- [WENO and hybrid shock-capturing schemes in scale-resolving simulation](/methods/weno-scheme.md)
- [Kinetic-energy preservation and split forms](/properties/kinetic-energy-preservation.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Shock-generated turbulence and turbulent shock jump relations](/results/shock-generated-turbulence.md)
- [FLEXI](/software/flexi.md)
- [GALÆXI](/software/galaexi.md)
- [PyFR](/software/pyfr.md)
