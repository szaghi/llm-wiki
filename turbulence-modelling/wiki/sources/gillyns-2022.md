---
type: Source
title: "Gillyns et al. (2022) — Implementation and Validation of an Algebraic Wall Model for LES in Nek5000"
description: "Implements an algebraic equilibrium wall-stress model, based on Reichardt's law with time-filtered input sampled at the top of the first spectral element, in the spectral element code Nek5000, and validates it in channel flow at Re_τ = 1000 and 5200 for different first-element heights and wall-normal meshes."
resource: "doi:10.1007/s10494-022-00378-y"
source_kind: paper
authors: [Gillyns E., Buckingham S., Winckelmans G.]
year: 2022
venue: "Flow Turbul. Combust. 109:1111-1131"
local_file: "/home/stefano/papers/mosaic/turbulence_modelling/2022_Crossref_Flow_Turbulence_and_Combustion_Gillyns_Implementation_and_Validation_of_an_Algebraic_Wall_Model_for.pdf"
tags: [wall-model, wmles, les, spectral-element]
timestamp: 2026-10-25T19:43:00Z
---

# Summary

Gillyns et al. (2022) implement an algebraic
[equilibrium wall model](/methods/equilibrium-wall-model.md) in the
open-source spectral element code Nek5000 and validate
[wall-modelled LES](/methods/wall-modelled-les.md) of the periodic
[channel](/benchmarks/turbulent-channel-flow.md) against the
[DNS](/definitions/direct-numerical-simulation.md) of Lee & Moser (2015) at
$Re_\tau=1000$ and $5200$. The LES uses polynomial degree $N=7$ and Nek5000's
approximate deconvolution SGS model (relaxation parameter `filterWeight` = 10).

The wall model samples the streamwise velocity at the last node of the
wall-adjacent element, at its upper edge. It filters this value in time with
an exponential moving average. It then inverts Reichardt's
[law of the wall](/definitions/law-of-the-wall.md) ($\kappa=0.38$, $B=4.1$)
for $u_\tau$ with a two-guess iteration and imposes $\tau_w$ through a
traction boundary condition in the stress formulation. Sampling inside the
first element keeps the model local to the element and avoids data transfer
between processes. The [LaRTE model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
of Fowler et al. (2022) is cited for the benefit of time-averaging the
wall-model input. Without the time filter the model diverges. A time constant
of $0.0025\,\delta/u_\tau$ (about five time steps) gives the same statistics
as $2\,\delta/u_\tau$, and it settles much faster.

The first-element height ($y^+=63$, 104, 153) hardly changes the results. The
error in the mean velocity is 0.52–1.09%, and in the normal stresses below 8%.
With four wall-normal elements per half channel, spikes in the fluctuation
statistics at element interfaces (a Gibbs phenomenon of the $C^0$ spectral
element basis) mark the mesh as under-resolved. At $Re_\tau=5200$ the mean
velocity error is below 1% and the fluctuation error at most 9%. The authors
attribute the accurate mean velocity inside the under-resolved first element
to the spectral element method. They present the Gibbs spikes both as a
reference-free mesh-quality indicator and as the method's main drawback. All
evidence is numerical, with no same-mesh comparison against another code.

# Version read

Version of record (Springer, open access CC BY 4.0; received 6 March 2022,
accepted 26 September 2022, published online 19 October 2022), 21 pages
(pp. 1111–1131), all read. Equations (1)–(7) were checked on the rendered
pages, because text extraction garbled (3), (5) and (6). Page 1 matches the
metadata, and there is no identity problem.

# Key claims

1. The number of grid points scales as $Re^{13/7}$ for wall-resolved LES and as $Re^{1}$ for WMLES, citing Choi & Moin (2012) and Yang & Griffin (2021) (§1). **Stated**
2. WMLES models the inner layer, $y/\delta\lesssim0.15$. The region $0.15\lesssim y/\delta\le1$ is constrained by the driving pressure gradient and by the shear stress propagated from the wall, so the inner layer can be replaced by the wall shear stress it would produce (§1). **Stated**
3. The simple algebraic model is expected to fail near or at separation. Under an adverse pressure gradient it is usable only while Coles' wake function has not reached the edge of the first element, referring to Frère et al. (2018) (§1). **Stated**
4. Wall-modelling guidelines for finite differences (Larsson et al. 2016) or DG (Frère et al. 2017) cannot be used as they are in a spectral element code: "the modelled region is highly sensitive to the discretization method" (§1). **Stated** (motivation)
5. The stress formulation of the momentum equation, Eq. (2), is required to prescribe the wall shear stress as a boundary condition. It is imposed with Nek5000's `sh` condition, `TRX = -(u_tau**2)*rho` (§2). **Stated**
6. The SGS model is Nek5000's approximate deconvolution model with `filterWeight` = 10, which "provided an excellent match with a DNS, as shown in Schlatter et al. (2004) at $Re_\tau\simeq210$". It uses high-pass filtering and is "not a simple eddy-viscosity SGS model" (§2). **Stated**
7. Polynomial degree 7 is used because Fischer (2013) indicates that it performs best for a wide range of applications (§2). **Stated**
8. In the spectral element method the velocity is $C^0$ across elements but its gradient is discontinuous. On coarse meshes this produces a Gibbs phenomenon, spikes in the gradient and in the velocity fluctuations at element boundaries, which vanishes as the mesh approaches DNS resolution. It can serve as a qualitative, reference-free mesh-quality indicator (§2, §6, §8). **Shown** (Figs. 8, 11, 13) / **Stated** (indicator use)
9. The input filter is the exponential moving average $\bar U_n=\bar U_{n-1}+\alpha_e(U_n-\bar U_{n-1})$ at each wall node, with $\alpha_e=\Delta t/(C_t+\Delta t)$ (Eq. 4; page-local symbols as on the [equilibrium wall model](/methods/equilibrium-wall-model.md) page). It is chosen over simple and weighted moving averages because it is memory-light, reactive and a first-order low-pass filter. Spanwise element-wise spatial averaging was tested and gave no significant improvement (§3). **Stated** (comparison not shown)
10. Reichardt's equation is inverted for $u_\tau$ by an iteration based on two initial guesses. It reaches machine precision in seven steps on average per wall node, at a cumulative cost of 0.4% of a time step, so a lookup table (Maheu et al. 2012; Frère et al. 2018) is unnecessary (§4). **Shown** (timing quoted, hardware not given)
11. Without time averaging ($C_t=0$) the wall model diverges, "most likely due to the Gibbs phenomenon at the element boundary creating high fluctuations in the sampled velocity" (§5). **Shown** (divergence) / **Stated** (cause)
12. With $C_t$ varied from 0 to $2\,\delta/u_\tau$ at $Re_\tau=1000$, $C_t=0.0025\,\delta/u_\tau$, the smallest nonzero value tested and equal to five time steps, "provides the best compromise". Its final solution is statistically equivalent to that of $C_t=2\,\delta/u_\tau$, which has a long settling time. The same $C_t$ is near optimal at $Re_\tau=5200$ (§5, §9). **Shown** (stated in the text; no figure of the sweep)
13. The instantaneous and filtered velocity fields at the sampling plane $y^+=153$ differ little: "the law of the wall is quite robust to the input quantity, yet it still requires a minimal time averaging". The short averaging time opens the way to unsteady flows (§5, Figs. 3–4). **Shown** (qualitative)
14. The streamwise and spanwise resolution is set by refining until the Gibbs spikes are small: 22×16 elements on $2\pi\delta\times\pi\delta$, i.e. $0.286\delta$ and $0.196\delta$ per element, average node spacings $0.040\delta$ and $0.028\delta$, and 24.5 and 35.7 nodes per $\delta$. This "provides similar results to the guidelines from Larsson et al. (2016)" (§6). **Stated**
15. Statistics are converged to at least 99.5% in the mean of the normal-stress profiles, judged with an exponential fit (§6, Fig. 5). **Shown**
16. With six elements per half channel at $Re_\tau=1000$, the first-element height is varied by tanh stretching ($y/\delta=0.063$, 0.10, 0.15; $y^+=63$, 104, 153). The mean velocity is "very well captured down to $y^+\simeq10$; only the first two nodes differ significantly", even inside the under-resolved first element (§7, Fig. 7). **Shown**
17. In the under-resolved first element, $R_{11}$ and $R_{33}$ do not go to zero at the wall at the first three nodes, while $R_{22}$ matches the DNS because the boundary condition sets the wall-normal velocity to zero (§7, Fig. 8). **Shown**
18. Table 1 gives the normalized RMS error, excluding the first three nodes, for stretching parameters 1.5/1.0/0.4: mean $u$ 0.52/0.65/1.09%; $R_{11}$ 2.82/3.27/4.30%; $R_{22}$ 6.86/7.67/7.09%; $R_{33}$ 7.94/7.42/7.73%; $u_\tau/u_b$ 0.37/0.42/0.87%. The errors grow slightly with the first-element height, which suggests "that using a first element height comparable to the end of the law of the wall region (here $y^+\simeq150$) is not necessarily the best choice" (§7). **Shown**
19. The first-element height "does not appear to have a significant impact on the solution" while it stays in the law-of-the-wall region ($y/\delta\lesssim0.15$), which makes the approach "quite flexible" (§7, §10). **Shown**
20. With the first element at $y/\delta=0.15$, 6, 5 and 4 elements per half channel (42, 35, 28 wall-normal nodes) give in Table 2: $u$ 1.09/0.82/0.89%; $R_{11}$ 4.30/5.22/5.03%; $R_{22}$ 7.09/4.57/6.32%; $R_{33}$ 7.73/3.53/5.23%; $u_\tau/u_b$ 0.88/0.73/0.79% (§8). **Shown**
21. The error is sometimes lower on coarser meshes because WMLES underpredicts the fluctuations in all cases and "the averaged value is artificially improved thanks to the amplified spikes". Four elements "must therefore be considered as not sufficiently resolved", and five are "acceptable" (§8). **Shown** / interpretation **Stated**
22. A spike in the fluctuations at the channel centre appears on all three meshes. It is attributed to the centre coinciding with an element interface where the gradient changes sign. Covering the centre with an element is left to future work (§8, Fig. 11). **Shown** (spike) / **Stated** (cause)
23. At $Re_\tau=5200$ with 20 uniform elements per half channel (first element ending at $y/\delta=0.05$, $y^+=260$) and 44×32 elements in the wall-parallel directions, the mean profile is well captured even in the under-resolved element. Table 3: $u$ 0.64%, $R_{11}$ 7.20%, $R_{22}$ 6.84%, $R_{33}$ 4.09%, $u_\tau/u_b$ 0.067% (§9). **Shown**
24. At $Re_\tau=5200$ with 10 elements per half channel (first element ending at $y/\delta=0.10$, $y^+=520$) and 22×16 elements, the mean profile is well captured in the resolved region and less so in the first element. Table 3: $u$ 0.56%, $R_{11}$ 9.00%, $R_{22}$ 8.26%, $R_{33}$ 6.79%, $u_\tau/u_b$ 0.312%. The Gibbs effect is larger, and $R_{33}$ differs most (§9). **Shown**
25. Overall the errors are below 1% on the mean velocity and 7–9% (worst case) on the fluctuations at both Reynolds numbers. "Regarding the outer region mesh requirements, the solution behaves similarly to a wrLES. No further limitations on the wall model are introduced" (§9, §10). **Shown** / **Stated**
26. The good mean profile inside the under-resolved first element "is likely due to the spectral element method". Low-order implementations and "even other types of high order discretizations, as found in the literature" do not necessarily achieve it (abstract, §1, §10). **Stated** (no same-mesh comparison with another discretization)

# Printed slips

- **Table 1 against Table 2.** The row for stretching parameter 0.4 in Table 1 and the row "6 elements" in Table 2 describe the same configuration (six elements, first element at $y/\delta=0.15$, §8). They agree in all profile errors (1.09, 4.30, 7.09, 7.73) but print the wall-stress error as 0.87% (Table 1) and 0.88% (Table 2).
- **§9 against Table 3.** The text says "The results show an error of < 1% on the mean velocity profile and < 9% on the velocity fluctuations", while Table 3 prints 9.00% for $R_{11}$ with 10 elements. The conclusion says "7-9% for the worst case".
- **Verdict on four elements.** §8 says "The case with 4 elements in the half channel height must therefore be considered as not sufficiently resolved to provide an accurate solution". §9 says "The case from $Re_\tau=1000$ with 4 elements in the half-channel height has noticeable Gibbs spikes; yet it remains a fair compromise between accuracy and computational cost".
- **Acronym.** "NMRSE" in §7, in §9 and in the caption of Table 3, against "NRMSE" in Eq. (6) and Tables 1–2.
- **§4 wording.** "it outputs the wall shear stress $u_\tau$": $u_\tau$ is the friction velocity.
- **Fig. 5.** The axis unit "time/LETOT" is not defined in the text.
- **Typos.** "thge present wmLES", "Argone National Laboratory", "ad at much higher Reynolds numbers" (§1); "has be tested" (§3); "for ensure proper convergence" (§6); "mwLES" (§8).
- **Reference list.** Fowler et al. (2022) is printed "J. Fluid Mech. 934, 871 (2022)" with DOI 10.1017/jfm.2021.1156; the article number of that DOI is A44. Larsson et al. (2016) is printed in "Mech. Eng. Rev.D 3(1), 15".

# Notation map

| Source | Registry ([notation](/notation.md)) | Note |
|---|---|---|
| $u$ (Eqs. 1–2) | $\bar u_i$ | LES fields written "omitting to use any complex notation" |
| $\tau=\mu[\nabla u+\nabla u^T]$ | $\sigma_{ij}=2\mu S_{ij}$ | molecular viscous stress (incompressible) |
| $\tau^{sgs}$ | (modelled SGS stress) | enters as $+\nabla\cdot\tau^{sgs}$ in Eq. (2) with no explicit definition, so it corresponds to $-\rho\tau_{ij}$ if the registry's positive-trace convention is meant; **collision** in sign |
| $p$ | $p$ | includes "any no-modelled trace of the SGS tensor" |
| $f$ | $f_i$ | forcing; the channel is run at constant flow rate |
| $u_\parallel$, $u_{\parallel_i}$ | $U_{\mathrm{LES}}$ | wall-parallel LES velocity at the top of the first element, node $i$ |
| $\overline{u}_{i_n}$ | $\bar U_n$ (page-local; $U_n$ the sampled $U_{\mathrm{LES}}$) | exponential moving average at time step $n$ (node index dropped) | **collision:** this overbar is a time filter, not the LES filter |
| $\overline{u'u'}$, $\overline{v'v'}$, $\overline{w'w'}$ | $R_{11}$, $R_{22}$, $R_{33}$ | here the overbar is a statistical average |
| $\alpha=\Delta t/(C_t+\Delta t)$ | $\alpha_e$ (filter weight, page-local) | **collision:** not the DG/FV blending factor |
| $C_t$ | (filter time constant) | in units of $\delta/u_\tau$; 0.0025 chosen |
| $\tau_w$, $\tau_{w_i}$, $\tau_{wall}$ | $\tau_w$ | three spellings |
| $u_\tau$, $u_\parallel^+$, $y^+$ | $u_\tau$, $U^+_{\mathrm{LES}}$, $y^+$ | $\tau_w=\rho u_\tau^2$ |
| $\kappa$, $C$ | $\kappa=0.38$, $B=4.1$ | values of Österlund et al. (2000); the paper notes $\kappa\simeq0.383$, $B\simeq4.25$ from Lee & Moser (2015) |
| $\delta$ | $\delta$ | channel half-height |
| $\gamma$ | (tanh stretching parameter, Eq. 7) | **collision:** neither the ratio of specific heats nor the intermittency |
| $y_u$ | (uniform wall-normal coordinate before stretching) | |
| $N$ | $N=7$ in §2 | **collision:** Eq. (6) uses $N$ for the number of points in the error sum |
| $u_{mean}$ | $u_b$ (bulk velocity, page-local) | |
| NRMSE | (normalized RMS error, Eq. 6) | normalized by the range of the DNS profile |
| $Re_\tau$ | $Re_\tau$ | $u_\tau\delta/\nu$ |

# Reference list

24 printed references in author–year style (alphabetical, Springer). The list
is merged complete into the [bibliography](/bibliography.md) with `citedby`
this slug. Two Nek5000 documentation items print the corporate author as
"Laboratory, A.N." and are entered under Argonne National Laboratory (2013,
2021). Fowler et al. (2022) is the already ingested
[Fowler et al. (2022)](/sources/fowler-2022.md), cited with a printed volume
and page that differ from the article number. Frère et al. (2018) is a PhD
thesis printed with its supervisors as co-authors and is recorded as printed.
Maheu et al. (2012) prints a title with no venue. Offermans et al. (2016)
takes its year from the conference name. Several items print only a DOI, and
Pal et al. (2022) prints its DOI twice. There are no printed duplicates and
no unparseable items.

# Pages created or updated

Chunk 2 (2026-10-25), cited further in chunks 3, 6. This source is cited on:

- [Turbulent channel flow](/benchmarks/turbulent-channel-flow.md)
- [Wall law in adverse pressure gradient](/definitions/adverse-pressure-gradient-wall-law.md)
- [Direct numerical simulation](/definitions/direct-numerical-simulation.md)
- [Large-eddy simulation: filtering and the subgrid-scale stress](/definitions/large-eddy-simulation.md)
- [Law of the wall](/definitions/law-of-the-wall.md)
- [Log-layer mismatch](/definitions/log-layer-mismatch.md)
- [Discontinuous Galerkin spectral element method](/methods/discontinuous-galerkin-spectral-element-method.md)
- [Equilibrium wall model](/methods/equilibrium-wall-model.md)
- [Lagrangian relaxation towards equilibrium (LaRTE) wall model](/methods/lagrangian-relaxation-towards-equilibrium-wall-model.md)
- [Scale-similarity and mixed subgrid-scale models](/methods/scale-similarity-model.md)
- [Continuous-Galerkin spectral-element method](/methods/spectral-element-method.md)
- [Wall-modelled large-eddy simulation](/methods/wall-modelled-les.md)
- [Numerical dissipation in scale-resolving simulation](/properties/numerical-dissipation.md)
- [Grid-point requirements of LES and DNS](/results/les-grid-point-requirements.md)
- [Nek5000 and NekRS](/software/nek5000.md)
