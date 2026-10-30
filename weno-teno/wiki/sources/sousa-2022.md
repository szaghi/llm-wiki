---
type: Source
title: "Sousa & Scalo (2022) — A unified Quasi-Spectral Viscosity (QSV) approach to shock capturing and large-eddy simulation"
description: "Proposes the quasi-spectral viscosity (QSV), one explicit, spectrally shaped eddy viscosity for sixth-order compact finite differences that serves both as an LES subfilter-scale closure and as shock capturing, built from Padé and Fejér filter residuals and tested against LAD and standard LES models."
resource: "doi:10.1016/j.jcp.2022.111139"
source_kind: paper
authors: [Sousa V.C.B., Scalo C.]
year: 2022
venue: "J. Comput. Phys. 459:111139"
local_file: "/home/stefano/papers/mosaic/weno-teno/2022_Crossref_Journal_of_Computational_Physics_C_A_unified_Quasi-Spectral_Viscosity_QSV_approach_to_shock_cap.pdf"
tags: [artificial-viscosity, turbulence, compact-scheme, finite-difference, numerical-dissipation, shock-capturing]
timestamp: 2026-10-22T20:00:00Z
---

# Summary

The paper proposes the [quasi-spectral viscosity (QSV)](/methods/quasi-spectral-viscosity.md),
a single explicit [artificial (eddy) viscosity](/methods/artificial-viscosity.md)
for a sixth-order compact Padé finite-difference discretization of the
Favre-filtered compressible Navier–Stokes equations, which acts both as the
subfilter-scale (SFS) closure of large-eddy simulation and as the shock-capturing
term. No reconstruction, Riemann solver or shock sensor is used.

§2 casts the dynamic Smagorinsky model, the Chollet–Lesieur spectral eddy
viscosity and Tadmor's spectral vanishing viscosity (SVV) in one form
(length scale × velocity scale × kernel convolved with the strain rate) and
argues that SVV is in effect an LES eddy viscosity for the filtered Burgers
equation. An a priori analysis of the filtered inviscid Burgers equation
([Burgers tests](/benchmarks/burgers-equation-tests.md)) shows that the exact
SFS energy flux of a forming shock has the "plateau-cusp" spectrum of
Kraichnan's turbulence theory, and that a model performs better the closer its
dissipation spectrum is to the exact one: the spectral shape of the added
[dissipation](/definitions/numerical-dissipation.md) decides accuracy.

QSV realizes this in physical space: the residual of a sixth-order Padé filter,
rescaled by an area ratio, estimates the energy at the grid cut-off direction by
direction and sets the viscosity magnitude; a blend of Padé and truncated Fejér
filter residuals imposes the plateau-cusp modulation on the strain rate and the
temperature gradient. The cut-off energy rises at shocks as at under-resolved
eddies, so no separate sensor is needed.

Shock capturing is tested on [Sod](/benchmarks/sod-and-lax-shock-tubes.md),
[Shu–Osher](/benchmarks/shu-osher-problem.md), a strong
[shock–vortex interaction](/benchmarks/shock-vortex-interaction.md) and shock
reflection off a sinusoidal wall at $M=1.5$ and $M=5$ ($\gamma=1.15$), against
the local artificial diffusivity (LAD) of Cook and Kawai–Lele; at $M=5$ LAD
breaks [symmetry](/properties/symmetry-preservation.md) early and QSV does not.
Turbulence modelling is tested on the subsonic
[Taylor–Green vortex](/benchmarks/taylor-green-vortex.md) and compressible
channel flows; the unified claim rests on the supersonic Taylor–Green vortex
($M_t=1.2$), where QSV alone is stable and closer to the reference than every
LES model aided by LAD. All evidence is numerical; nothing is proved.

# Version read

arXiv 2111.01929v2 [physics.flu-dyn], 13 March 2022, the authors' preprint in
the Elsevier template ("Received 23 March 2021", no volume or article number),
35 pages, all read; equations on pp. 5, 6, 9–14 and 17 checked visually. Not
the version of record. Page 1 matches Crossref in title and authors; page 1
prints "Victor C. B. Sousa", whose family name Crossref records as
"C. B. Sousa" (hence the archive filename `..._C_...`). The DOI is not printed
on the preprint. Equation, figure and section numbers cited here are those of
this version.

# Key claims

Registry notation is used where the registry has a symbol; the LES symbols
(filter $\overline{\,\cdot\,}$, Favre filter $\check{\,\cdot\,}$, SFS stress
$\tau_{ij}$, cut-off wavenumber $k_c$, transfer functions
$\widehat{\widetilde G}$) have no registry counterpart and are kept as in the
source (see the notation map).

1. Dynamic Smagorinsky, spectral eddy viscosity and SVV all fit the generalized SFS form $\tau_{ij}=\ell\,\upsilon_c\,(K*S_{ij})$ with the entries of Table 1 (§2.2, Eq. 17, Table 1). **Derived**
2. Adding an SVV term to Burgers' equation (Eq. 13) is formally the same as closing the filtered Burgers equation (Eq. 7) with an eddy viscosity; it differs from the LES models only in the spectral make-up of the modelled term. This explains why SVV worked when extended to turbulent LES, which earlier work had left unexplained (§2.2, §8). **Derived**
3. The spectral eddy viscosity can be rewritten in physical space as the residual of a test filter, $-\tau^d_{ij}=\sqrt{2\overline\Delta E_{k_c}}\,\big((1-\widetilde G)*\overline S_{ij}\big)$, which makes its kinship with Germano's dynamic procedure explicit (§2.2, Eqs. 11–12). **Derived**
4. For the filtered inviscid Burgers equation at $t=1$, $N_x=128$, the exact SFS energy flux spans all resolved wavenumbers and peaks near $k_c$: a plateau-cusp shape like that of Kraichnan and Chollet–Lesieur for turbulence, here produced by shock formation (§2.3, Fig. 1b). **Shown**
5. Dynamic Smagorinsky gives a flat broadband dissipation spectrum, over-dissipating large scales and under-dissipating near the cut-off; a posteriori this gives high-wavenumber pile-up and oscillations in the Burgers solution (§2.3, Fig. 1). **Shown**
6. SVV with an inviscid low-wavenumber range ($m=5\sqrt{k_c}$) underdamps the low wavenumbers a priori and a posteriori accumulates energy near the cut-off and oscillates near the discontinuity; the larger the inviscid range, the worse; SVV with $m=0$ is better (§2.3, Fig. 1). **Shown**
7. "The closer the spectral content of the added dissipation is to the exact SFS stresses, the better is the performance of the model in solving for the resolved flow scales" (§2.3). **Shown** (on one Burgers case)
8. The residual of the sixth-order Padé filter, scaled by $A(\alpha)/A(\alpha_{k_c})$, estimates the cut-off energy; a larger filter parameter concentrates the residual near $k_c$ but widens it in physical space; $\alpha=0.45$ is used throughout, and $\alpha_{k_c}=0.4994$ for $k_c=64$ (§3.1, Eqs. 23–26, Fig. 2). **Derived** (closed form of $A(\alpha)$, Eq. 25) / **Shown**
9. The spatial Fejér filter truncated to a half-width of $n_w=8$ points has a transfer function that converges quickly to $1-k/k_c$ because its weights decay by themselves ("self-windowed"), so truncation and non-periodic boundaries are usable (§3.2, Fig. 3). **Shown**
10. The QSV modulation $\widehat{\widetilde G}_{\rm qsv}=w\big[1-\beta\widehat{\widetilde G}_{\rm Pad\acute e}(\alpha)+(1-\beta)\widehat{\widetilde G}_{\rm Fej\acute er}\big]$ with $\alpha=0.45$, $\beta=0.8$, $w=0.85$ is tailored to the plateau-cusp shape; the parameters are tuned on Burgers and checked against exact a priori SFS spectra of the Taylor–Green vortex (Fig. 12) and Sod (Fig. A.21) (§3.2, Eq. 35). **Shown**
11. As constructed, from an a priori analysis with sharp spectral filters, the model "is only suitable for spectral or quasi-spectral high-order discretizations"; a low-order code needs its own a priori analysis with a different primary filter (§3.2). **Stated**
12. The constants are $C_{\tau_{ij}}=1.0$ ($i=j$), $0.6$ ($i\ne j$) and $C_q=0.8$, informed by a priori analyses of Sod and the Taylor–Green vortex, whose exact SFS stress has larger trace than off-diagonal components at all wavenumbers up to $k_c$ (§4.2, Eq. 51; §6.1, Fig. 12). **Shown**
13. On Sod ($t=0.2$, grid study) QSV and LAD both converge, QSV with slightly sharper discontinuities on equal grids; LAD needs an explicit Padé filter ($0.495$), QSV does not (an optional filter, $0.499$, removes residual high-wavenumber oscillations) (§5.1, Fig. 4). **Shown**
14. On the Shu–Osher problem ($t=0.36$, reference QSV on 4096 points) QSV and LAD recover the post-shock density oscillations similarly; QSV gives a sharper shock, especially in the velocity, and converges monotonically from very coarse grids (§5.1, Fig. 5). **Shown**
15. On the strong shock–vortex interaction both QSV and LAD miss the asymmetric vortex splitting on $192\times96$, are qualitatively right on $384\times192$ and converge to the same result; QSV gives a sharper shock and less noise but underestimates the post-shock top-vortex core size on $384\times192$; QSV sustains the shock on a sinusoidally distorted grid (§5.2, Figs. 6–7). **Shown**
16. For shock reflection off a sinusoidal wall at $M=1.5$ ($1024\times256$) QSV reproduces the triple points, Mach stems and slip lines with 8 times fewer degrees of freedom than Tonicello et al. (2020); the spurious contact from the sharp initial jump is much weaker than with LAD, which also oscillates near the primary vortex and smears a secondary vortex that QSV captures (§5.3, Figs. 8–9). **Shown**
17. At $M=5$, $\gamma=1.15$, LAD shows strong spurious oscillations and early symmetry breaking, QSV preserves symmetry: QSV has "similar resolution capability as the established LAD model but with higher degrees of robustness in the presence of stronger shock intensities" (§§5.3–5.4, Figs. 10–11). **Shown**
18. On the subsonic Taylor–Green vortex ($M_t=0.1$, $\mathrm{Re}=5000$, $96^3$) the run without a model diverges near $tV_0/L\approx10$; QSV is closer to filtered DNS than dynamic Smagorinsky and CvP from $tV_0/L\approx6$, with slight over-damping before, and only QSV recovers the post-peak dissipation plateau (§6.1, Fig. 13). **Shown**
19. A priori on the Taylor–Green vortex ($384^3$ DNS, sharp filter at $k_c=48$), QSV fed with filtered DNS regulates the SFS dissipation magnitude in time and reproduces the plateau-cusp shape closely (§6.1, Fig. 12). **Shown**
20. Cost on the $96^3$ Taylor–Green vortex relative to no model: Smagorinsky +34.3%, CvP +37.7%, QSV with only $\tau_{ij}$ +64.7%, dynamic Smagorinsky +72.5%, full QSV +78.5% (hardware not stated) (§6.1, Table 2). **Shown**
21. QSV-LES of the $M_t=0.1$ Taylor–Green vortex improves monotonically with the grid ($72^3$ to $144^3$) against filtered DNS (§6.1, Fig. 14). **Shown**
22. In compressible channel flow ($M_b=1.5$, $\mathrm{Re}_b=5000$; $M_b=6.0$, $\mathrm{Re}_b=20000$) QSV and Vreman's model both capture the viscous sublayer; in the log region Vreman's model is closer to the log law and DNS on every grid; at $M_b=6.0$ the difference is small, and Vreman's model needed LAD for stability while QSV did not. QSV "may not be the best choice for simple wall-bounded turbulent flows up to supersonic speeds" (§§6.2–6.3, Fig. 15, Table 3). **Shown**
23. In the supersonic Taylor–Green vortex ($M_t=1.2$, $\mathrm{Re}=5000$) the volume-averaged kinetic energy is non-monotonic with negative "dissipation", while Myers' exact compressible energy norm decays monotonically, so the latter is the right norm (§7.1, Figs. 17–18). **Shown**
24. Without shock capturing, every LES model (none, Smagorinsky, dynamic, CvP) blows up on the $M_t=1.2$ Taylor–Green vortex at $96^3$, while QSV runs stably; with LAD added, all LAD-aided runs over-dissipate near $tV_0/L\approx6.5$ (the strongest shocks) and underpredict the dissipation peak, while QSV stays closest to the $384^3$ QSV reference throughout; LAD alone becomes unstable without its artificial shear viscosity (§7.1, Fig. 19). **Shown**
25. Because a DNS is "not strictly possible" with shocks present, the $384^3$ QSV run is the reference, justified by the grid convergence of QSV and of LAD-aided Smagorinsky (§7.1, Fig. 18). **Stated** / **Shown**
26. QSV extends to curvilinear grids (Appendix B) and could extend to unstructured spectral-element solvers, where projection on a hierarchical orthogonal basis would give the cut-off energy and the modulation without global filters (§5.2, §8, App. B). **Stated** (curvilinear formulation **Derived**)

# Printed slips

- Eqs. 30–32, Fejér filter: Eq. 30, $\frac1{2k_c}\sum_{k=-k_c}^{k_c}(1-|k|/k_c)c_k^{-1}e^{\mathrm ik\theta}$, gives the diagonal weight $\tfrac12$ at $\theta=0$, while the closed forms Eqs. 31–32 give $\frac{4+2k_c}{2(2+2k_c)}$ ($0.5077$ at $k_c=64$). The weights of Eq. 32 have unit sum and discrete Fourier transform $1-|k|/(k_c+1)$, so the closed form is the Fejér mean with denominator $k_c+1$, not the $1-k/k_c$ of Eqs. 27–30: an $O(1/k_c)$ inconsistency. *(compiler check, not in the sources: closed-form sum of Eq. 30 at $\theta=0$, and DFT of the Eq. 32 weights for $k_c=8$.)*
- Eqs. 29–30 print the factor $(1-k/k_c)$ for $k$ from $-k_c$ to $k_c$; Eq. 27 defines $\sigma_1(\eta)$ only for $\eta\in[0,1]$, so $\lvert k\rvert$ is meant.
- After Eq. 31: "would be done by solving $u^{\sigma_1}=H_{ij}u_j$ where $G_{{\rm Fej\acute er},ij}=\dots$" — $H_{ij}$ is undefined; it is $G_{{\rm Fej\acute er},ij}$.
- p. 5: the spectral-eddy-viscosity length scale "$1/k_c\approx2\overline\Delta$" conflicts with $k_c=\pi/\Delta$ (Eqs. 22, 34), which gives $1/k_c=\Delta/\pi$; Eq. 12 uses the $2\overline\Delta$ reading.
- Eq. 17 is printed $\tau_{ij}=\ell\upsilon_c(K*S_{ij})$, without the minus sign that Eqs. 8, 11, 12, 19 and 47 carry.
- §4.2, p. 14: "The suggested constants (all of unitary value)" contradicts Eq. 51 ($C_{\tau_{ij}}=0.6$ off the diagonal, $C_q=0.8$).
- Eq. 26 writes the velocity $\overline u_j$, Eq. 46 $\check u_j$ (filter against Favre filter).
- Text: "It can be observed, in 1 b)" (figure reference missing, §2.3); "for for" in the title of §2; "He proposed" for the four-author Moin et al. (1991); Eq. 77 is an empty numbered line.

# Notation map

| Sousa & Scalo (2022) | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $\overline f$, $\overline\Delta$, $\Delta$ | kept; $\Delta x$ | LES filter and filter width; grid spacing $\Delta$ is $\Delta x$ |
| $\check f=\overline{\rho f}/\overline\rho$ | kept | Favre filter |
| $\widetilde f$ | kept | **overloaded: Padé-filtered field (Eq. 20) and Favre filter of a product (Eq. 41)** |
| $\tau_{ij}$, $\tau^d_{ij}$ | kept (LES) | SFS stress and its deviator; **not the registry's WENO-Z global indicator $\tau$** |
| $q_j$ | $\mathfrak q_j$ (page-local) | SFS temperature flux; **$q$ is the weight exponent in the registry** |
| $\nu_t$, $\nu^+_t$ | kept | eddy viscosity and SEV kernel; **$\nu$ is the CFL number in the registry** |
| $k$, $k_c=\pi/\Delta$ | $k_w$, kept | wavenumber; $k/k_c=\vartheta/\pi$ |
| $E_{k_c}$, $E^i_{k_c}(\check u_j)$ | $E_{k_c}$, $\mathsf E^{(i)}(v_j)$ (page-local) | cut-off energy; **$E$ is the total energy in the registry** |
| $\ell$, $\upsilon_c$, $K$ | $\ell$, $\upsilon$, $\mathcal K$ (page-local) | generic length, velocity scale and kernel (Eq. 17); **$K$ is the TENO stencil size in the registry** |
| $\widetilde G$, $\widehat{\widetilde G}$ | $\widetilde G$, $\hat G_{\mathrm P}$, $\hat G_{\mathrm F}$, $\hat G_{\mathrm{qsv}}$ (page-local) | test filter and its transfer function (Padé, Fejér, QSV); **$G$ is the admissible set in the registry** |
| $\alpha$, $\alpha_{k_c}$, $A(\alpha)$ | $\alpha_{\mathrm P}$, $\alpha_{k_c}$, $A(\alpha_{\mathrm P})$ (page-local) | Padé filter parameter, its optimal value, area under the residual; **$\alpha$ collides with $\alpha_k$ and with the DG–FV blending coefficient** |
| $a_j$ | kept | filter coefficients; **$a$ is the maximum wave speed in the registry** |
| $\sigma_p(\eta)$, $\eta=k/k_c$, $c_k$, $n_w$ | kept | Vandeven filter, aliasing factor, Fejér half-width; **$\eta$ is the entropy in the registry** |
| $\beta$, $w$ | $b_{\mathrm F}$, $w_{\mathrm{DC}}$ (page-local) | blend weight and offset of $\widehat{\widetilde G}_{\rm qsv}$; **$\beta$ collides with $\beta_k$, $w$ with the entropy variables** |
| $\mathcal D_{ij}$, $\ddot u_i$, $\ddot T$ | $\mathcal D_{ij}$, $\breve\partial_jv_i$, $\breve\partial_jT$ (page-local) | dissipation magnitude tensor and modulated gradients |
| $C_{\tau_{ij}}$, $C_q$, $C$ | $C_{\tau,ij}$, $C_q$, $C$ | model constants; Smagorinsky coefficient $C$ (**not the TENO constant**) |
| $Q$, $\epsilon$, $m$ | $\mathcal K_{\mathrm{SV}}$, $\epsilon_{\mathrm{SV}}$, kept (page-local) | SVV kernel, amplitude and activation wavenumber; **$\epsilon$ is the weight regularization in the registry and the SFS heat dissipation of Eq. 44 in the source** |
| $u_i$, $u$ | $v_i$, $v$ | velocity |
| $N$ | $N_x$ | Fourier modes of the Burgers analysis |
| $\gamma$, $M$, $\mathrm{Re}$ | $\gamma$, $M$, $\mathrm{Re}$ | agrees; $M_t$, $M_b$, $\mathrm{Re}_b$ kept |
| $E_c$, $\epsilon_c$ | kept | Myers' compressible energy norm and its dissipation rate |

# Reference list

55 printed references in Elsevier author–year style (alphabetical), all parsed
and merged complete into the [bibliography](/bibliography.md) with `citedby`
`sousa-2022`. Premasuthan et al. 2014a/2014b take the keys `premasuthan-2014`
and `premasuthan-2014-b`. DOIs are printed only for Gupta & Scalo 2018, Lele
1992 and Lodato et al. 2017 (printed "in press"); Chen & Scalo 2021 prints
volume 920 without a page or article number, Pasquetti 2005 volume 6 without
a page, and Morkovin 1962 "Mécanique de la Turb. 367, 380". No printed
duplicates were found.

# Pages created or updated

Chunk 3 (2026-10-22), cited further in chunks 4–12 (2026-10-22/30). This source is cited on:

* [Artificial viscosity and spectral viscosity](/methods/artificial-viscosity.md)
* [Burgers equation tests](/benchmarks/burgers-equation-tests.md)
* [Numerical dissipation and anti-dissipation](/definitions/numerical-dissipation.md)
* [Quasi-spectral viscosity](/methods/quasi-spectral-viscosity.md)
* [Shock–vortex interaction](/benchmarks/shock-vortex-interaction.md)
* [Shu–Osher shock–entropy-wave problem](/benchmarks/shu-osher-problem.md)
* [Sod and Lax shock tubes](/benchmarks/sod-and-lax-shock-tubes.md)
* [Symmetry preservation](/properties/symmetry-preservation.md)
* [Taylor–Green vortex](/benchmarks/taylor-green-vortex.md)
* [Troubled-cell and shock indicators](/definitions/troubled-cell-indicator.md)
